/* Üye hesabı eşitleme (Hit Pazarı).
   Google ile giriş yapan kişinin beğenileri, teklifleri ve iletişim bilgisi Firestore'da
   uyeler/{uid} belgesinde tutulur; telefon, web ve başka cihaz aynı listeyi görür.
   Yerel kayıt (localStorage 'halalar-app-v1') her sayfada aynen kullanılmaya devam eder;
   bu dosya yalnız onu hesapla eşitler. Sayfa kendi firebase.initializeApp'ini yaptıktan sonra yüklenmeli. */
(function(){
  const KEY='halalar-app-v1';
  if(typeof firebase==='undefined'||!firebase.apps||!firebase.apps.length||!firebase.auth||!firebase.firestore)return;
  const auth=firebase.auth(),db=firebase.firestore();
  const oku=()=>{try{return JSON.parse(localStorage.getItem(KEY))||{}}catch(e){return {}}};
  const yaz=x=>{try{yerelYaz.call(localStorage,KEY,JSON.stringify(x))}catch(e){}};
  const temiz=x=>({
    begeni:(x.begeni||[]).filter(i=>typeof i==='string').slice(-500),
    islem:(x.islem||[]).slice(0,200).map(t=>({id:String(t.id||''),ref:String(t.ref||''),tur:t.tur==='alim'?'alim':'teklif',tutar:Number(t.tutar)||0,durum:String(t.durum||'Beklemede'),zaman:Number(t.zaman)||0,satici:/^d2:/.test(String(t.id))?'dukkan2':/^d3:/.test(String(t.id))?'dukkan3':'halalar'})),
    kisi:{ad:String((x.kisi&&x.kisi.ad)||'').slice(0,59),tel:String((x.kisi&&x.kisi.tel)||'').replace(/[^0-9+]/g,'').slice(0,16)}
  });
  let uid=null,bekle=null,hazir=false;
  function gonder(){ if(!uid||!hazir)return; const t=temiz(oku());
    db.collection('uyeler').doc(uid).set(Object.assign(t,{guncel:firebase.firestore.FieldValue.serverTimestamp()})).catch(e=>console.warn('hesap eşitlenemedi',e)) }
  // yerel kayıt her değiştiğinde (beğeni, teklif, bilgi) 1,5 sn sonra hesaba yaz
  const yerelYaz=Storage.prototype.setItem;
  Storage.prototype.setItem=function(k,v){yerelYaz.call(this,k,v);if(this===localStorage&&k===KEY&&uid){clearTimeout(bekle);bekle=setTimeout(gonder,1500)}};
  auth.onAuthStateChanged(async u=>{
    uid=u?u.uid:null;hazir=false;if(!u)return;
    try{
      const s=await db.collection('uyeler').doc(u.uid).get(),uz=s.exists?s.data():{},yer=oku();
      // birleştir: beğeniler birleşimi, teklifler belge no'ya göre, bilgiler önce bu cihaz
      const beg=[...new Set([...(uz.begeni||[]),...(yer.begeni||[])])];
      const isl=[...(yer.islem||[])];const var_=new Set(isl.map(t=>t.ref||t.id+'@'+t.zaman));
      (uz.islem||[]).forEach(t=>{const k=t.ref||t.id+'@'+t.zaman;if(!var_.has(k)){isl.push(t);var_.add(k)}});
      isl.sort((a,b)=>(b.zaman||0)-(a.zaman||0));
      const kisi=(yer.kisi&&yer.kisi.ad)?yer.kisi:(uz.kisi&&uz.kisi.ad?uz.kisi:yer.kisi);
      const yeniGeldi=beg.length>(yer.begeni||[]).length||isl.length>(yer.islem||[]).length||(kisi&&!(yer.kisi&&yer.kisi.ad)&&kisi.ad);
      Object.assign(yer,{begeni:beg,islem:isl});if(kisi)yer.kisi=kisi;
      yaz(yer);hazir=true;gonder();
      // hesaptan yeni bilgi geldiyse sayfa ekranı eski veriyle kalmasın: bu oturumda bir kez tazele
      if(yeniGeldi&&!sessionStorage.getItem('uye-tazelendi')){sessionStorage.setItem('uye-tazelendi','1');location.reload()}
    }catch(e){console.warn('hesap okunamadı',e);hazir=true}
  });
})();
