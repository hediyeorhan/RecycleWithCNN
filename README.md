<h2> VERİ SETİ </h2>
 Veri seti için https://github.com/garythung/trashnet adresindeki veriler kullanılmıştır. DataAugmantation.ipynb dosyasında bulunan kodlar ile verilere artırma işlemi uygulanmıştır ve yaklaşık olarak 2 katına çıkarılmıştır.
 
 <h2> PROJENİN YAPIM AŞAMALARI, KARŞILAŞILAN SORUNLAR VE İZLENİLEN YOLLAR </h2>
 <h5> Okulda proje dersimiz kapsamında geliştirdiğim projemin yapımı esnasında izlenilen yollar ve planlardan bahsedilecektir. <h5>

Projede kullanılabilecek veriler ile ilgili veri seti araştırılması yapıldı. Kaggle sitesi üzerinden ulaşılan veri seti ile github reposu üzerinden ulaşılan veri seti karşılaştırıldı ve değerlendirildi. Github reposu üzerinden ulaşılan verilerin model eğitimi için daha uygun olduğu düşünüldü ve kullanılacak veri seti olarak bu veriler seçildi. Veri setinin seçilmesinde görsellerin arka plan, çözünürlük gibi özellikleri göz önünde bulunduruldu. Verileri kullanmak için gerekli izinler alındı. Verilerin yeterliliğinin değerlendirilmesi için planlama yapıldı. Kullanılacak veri seti 5 kategoriden oluşmaktadır. Kategoriler cam, karton, metal, plastik ve kâğıt türleridir. Her kategorideki veri sayıları yaklaşık olarak birbirine yakındır, toplamda 2392 adet veri bulunmaktadır. 

![image](https://user-images.githubusercontent.com/59260491/176998405-1c6d0a2f-2ffc-4a3d-8eb6-54a298ee6c2f.png)
	
<h5> Şekil 1 : Kullanılan veri setinden örnekler </h5>

Elimizde bulunan veri seti ile CNN modeli eğitildi. YOLO  ve SSD algoritmalarının etiketleme ve tespit yönünden gerekli olmadığına karar verildi. CNN algoritmalarının sınıflandırma problemine daha uygun olduğuna karar verildi. Veri setini test etmek amaçlı eğitilen model dosyası test verileri ile test edildi. Veri setinin eğitimine başlamadan önce veri seti %80 train  ve %20 test olmak üzere iki parçaya ayrılmıştır. Veri setini bu şekilde ayırmamızın nedeni, eğitim bittikten sonra oluşan model dosyamızın başarısını ölçmektir. Validation verisi ayırılmadı çünkü gerek duyulmadı. Validation verisi sayesinde eğitim sırasında modelin doğruluk değerleri görülebiliyor fakat burada train verisinin daha fazla olması amaçlanmıştır ve veri seti iki parçaya ayrılmıştır. CNN modelinin iterasyon sayısı, katman sayısı gibi değerlerinin değiştirilmesine ve farklı iterasyonlarda model eğitilmesine karar verildi. Şu anki süreçte CNN üzerinden model eğitimine devam edilecektir. Model doğruluk değeri için iyileştirmeler yapılacaktır. Veri setinin eğitim aşamasında Google Colaboratory  ortamı kullanılacaktır çünkü Google ücretsiz olarak GPU desteği sağlamaktadır. Bu sayede eğitimler daha hızlı bir şekilde gerçekleşmektedir.

Önceki planlananlar doğrultusunda bir cnn modeli oluşturuldu. Epoch sayısı ilk eğitimde 500 olarak belirlendi. Şekil 2’de oluşturulan modelin katmanlarını inceleyelim.

![image](https://user-images.githubusercontent.com/59260491/176998458-d018da9a-a338-4cb0-b08f-554f2abdd316.png)
	
<h5> Şekil 2: Oluşturulan sinir ağı modeli </h5> 
	
Oluşturulan modelde verilerin giriş boyutu (128,128,3) olarak verilmiştir burada 3 değeri rgb renk kodlarından gelmektedir. Veriler siyah beyaz bir yapıda olsaydı 3 yerine 1 kullanılmalıydı. Modelin overfittinge uğramasını engellemek amacıyla Dropout katmanı eklenmiştir. Dropout genelde tam bağlı katmanlarda (fully-connected layer) sonra kullanılır. Dropout kullanılarak fully-connected layerlardaki bağlar koparılır. Böylece node'lar birbiri hakkında daha az bilgiye sahip olur ve bunun doğal sonucu olarak node'lar birbirlerinin ağırlık değişimlerinden daha az etkilenirler. Flatten katmanının görevi basitçe, son ve en önemli katman olan Fully Connected Layer’ın girişindeki verileri hazırlamaktır. Dense katmanında verilen 5 değeri veri setindeki kategori sayısıdır. Son olarak eğitim kısmında callback eklenmiştir bunun sebebi ise eğitim aşamasında istediğimiz accuracy ve loss değerleri alındığında eğitimin durdurulmasını sağlamaktır.
Modelde kullanılan iki önemli katman da convolutional layer ve pooling layer’dır. Convolutional layer katmanında girdi olarak gelen resim bir filtreden geçirilir. Filtreden geçirilme sonucu oluşan değerler öznitelik haritasını oluşturur. Input olarak elimizde 4x4 lük matris vardır. Belirlenen filtre ise 2x2 boyutundadır. Burada input olarak gelen matrisin tamamında bu filtre gezdirilerek, input üzerinde oluşan her 2x2 matris ile filtre matrisi çarpılarak öznitelik matrisi oluşturulur. Birden fazla filtre olması durumunda bu işlemler her bir filtre için uygulanır. Genel olarak convolutional katmanı ile resimlerdeki sadece gerekli ve önemli olan öznitelikler belirlenir. Farklılık oluşturmayan öznitelikler ise hesaba dahil edilmez.
 
![image](https://user-images.githubusercontent.com/59260491/176998477-94a32c64-bec8-4293-8876-40acdd8ef2ad.png)
	
<h5> Şekil 3: Convolutional Layer </h5> 

Convolutional layer’dan sonra ikinci katman pooling layer’dır. Bu katman, CovNet’teki ardışık convolutional katmanları arasına sıklıkla eklenen bir katmandır. Bu katmanın görevi, gösterimin kayma boyutunu ve ağ içindeki parametreleri ve hesaplama sayısını azaltmak içindir. Bu sayede ağdaki uyumsuzluk kontrol edilmiş olur. Bizim burada kullandığımız maxpooling algoritmasıdır. Yine aynı prensipte çalışan average pooling, ve L2-norm pooling algoritmaları da vardır.
 
![image](https://user-images.githubusercontent.com/59260491/176998481-ef9b3694-fa7d-45c8-96de-34cec9a052d2.png)
	
<h5> Şekil 4: MaxPooling </h5> 

Eğitimler sonucu elde edilen değerleri inceleyelim.

 ![image](https://user-images.githubusercontent.com/59260491/176998605-a051c5cd-9c0a-441c-8af2-bb0431ab8a49.png)
	
<h5> Şekil 5: 500 epoch sonucu elde edilen değerler </h5> 

Epoch sayısı fazla arttırıldığı zaman modelin overfittinge uğradığı düşünüldü. Bu durumdan emin olmak için 800 epoch ile aynı sinir ağı kullanılarak bir model daha eğitildi.

 ![image](https://user-images.githubusercontent.com/59260491/176998615-40d611ed-13fb-4a7d-8d9d-c5b4f0007231.png)
	
<h5> Şekil 6: 800 epoch sonucu elde edilen değerler </h5> 
	
Grafiklerdeki sonuçlar incelendiğinde 500 epoch ve 800 epoch arasında modeli iyileştirecek derecede bir fark olmadığı görülmüştür. Elde edilen bu sonuçlar doğrultusunda mobilenet algoritması  ve vgg algoritması modellerinin kullanılmasına ve sonuçlarının incelenmesine karar verildi.
	
Son eğitimler sonucunda fazla epoch sayısının overfittinge sebep olduğu düşünüldü ve bu yüzden epoch sayısı 100 olarak güncellendi. Öncelikli olarak 100 epoch ile bir eğitim gerçekleştirildi. Gerçekleştirilen eğitim sonucunda test loss değeri 1.985 ve test accuracy değeri 0.6860 olarak elde edildi. Şekil 7’te eğitim sonucunda elde edilen confusion matrix  verilerini inceleyelim. Confusion matrix makine öğrenimi alanında ve özellikle istatistiksel sınıflandırma probleminde, bir hata matrisi olarak da bilinen bir karışıklık matrisi, tipik olarak denetimli bir öğrenme algoritması olan bir algoritmanın performansının görselleştirilmesine izin veren özel bir tablo düzenidir.

![image](https://user-images.githubusercontent.com/59260491/176998631-10d9e035-e5c0-4978-a903-999d1b238189.png)
 
<h5> Şekil 7: Confusion Matrix verileri </h5> 


Eğitimin doğruluk ölçüsü olarak f1-score değerlerine bakıldığında istenilenden çok düşük olduğu görülmüştür. Confusion matrix’te sonuçlar aşağıdaki dört kritere göre değerlendiriliyor.
Gerçek Pozitifler (TP): Bunlar gerçek değeri 1 ve tahmin ettiğimiz değerin de 1 olduğu örneklerdir. 
Gerçek Negatifler (TN): Bunlar gerçek değeri 0 ve tahmin ettiğimiz değerin de 0 olduğu örneklerdir.
Yanlış Pozitifler (FP): Bunlar gerçek değeri 0 ancak tahmin ettiğimiz değerin 1 olduğu örneklerdir. 
Yanlış Negatifler (FN): Bunlar gerçek değeri 1 ancak tahmin ettiğimiz değerin 0 olduğu örneklerdir.
  
![image](https://user-images.githubusercontent.com/59260491/176998646-50ae199b-fce7-4ebb-b503-ca7f986fdf50.png)
	
<h5> Formül 1  </h5>   
	
![image](https://user-images.githubusercontent.com/59260491/176998651-947307f8-605a-47af-b9b4-98db845404d5.png)
	
<h5> Formül 2 </h5> 
	
![image](https://user-images.githubusercontent.com/59260491/176998655-2a6dbb14-c8b4-4dc8-a983-43905d18ffca.png)
	
<h5> Formül 3 </h5> 
                                   
 
Doğruluk (Accuracy) yerine F1 Score değerinin kullanılmasının en temel sebebi eşit dağılmayan veri kümelerinde hatalı bir model seçimi yapmamaktır. Ayrıca sadece False Negative ya da False Positive değil tüm hata maliyetlerini de içerecek bir ölçme metriğine ihtiyaç duyulduğu içinde F1 Score çok önemlidir.
 
![image](https://user-images.githubusercontent.com/59260491/176998688-fb774f14-c8a5-4ba3-aebf-658abbdf0818.png)
	
<h5> Şekil 8: 100 epoch sonucu elde edilen değerler </h5> 

İkinci olarak 80 epoch ile bir eğitim daha gerçekleştirildi. Bu eğitimde callback yerine earlystop fonksiyonu kullandıldı. EarlyStop ile eğitim 25 epoch sonucunda sonlandı. Test loss değeri 1.10 ve test accuracy değeri 0.65 olarak elde edildi. Değerlerden farkedileceği üzere 100 epoch ve 25 epoch arasında da çok fazla bir fark olduğu görülmemiştir. 
 

![image](https://user-images.githubusercontent.com/59260491/176998699-8a497cac-880e-486b-813d-e4fa5e831c78.png)

<h5> Şekil 9: 25 epoch sonucu elde edilen değerler </h5> 
	
Üçüncü olarak mobilenet modeli kullanılarak bir eğitim gerçekleştirilmiştir. 

![image](https://user-images.githubusercontent.com/59260491/176998713-b69bf7fd-4ae7-4eed-8f0d-434ffdf3a4f2.png)
	
<h5> Şekil 10: MobileNet yapısı </h5> 
 
![image](https://user-images.githubusercontent.com/59260491/176998723-0b747802-d75d-4f6a-8f9a-68fff17de9b6.png)
	
<h5> Şekil 11: MobileNet ağ mimarisi </h5> 
	
120 epoch olarak tasarlanan modele earlystop eklenmiştir. Değerler stabil bir hale geldiğinde eğitim 77 epoch’da durdurulmuştur. Test accuracy değeri 0.8752 , F1-Score değeri 0.8876, Recall değeri 0.8730 olarak elde edilmiştir.

![image](https://user-images.githubusercontent.com/59260491/176998745-88aa9838-7cac-43b3-b3a8-a29e2d2ad21f.png)
	
<h5> Şekil 12: MobileNet kullanılarak oluşturulan model </h5> 

![image](https://user-images.githubusercontent.com/59260491/176998759-772ff30c-02b0-46b5-988f-305bc200acd8.png)
	
<h5> Şekil 13: MobileNet eğitimi sonucunda elde edilen değerler </h5> 
	
Şekil 13’de confusion matrix sonucunda elde edilen veriler incelendiğinde f1-score değerinin gayet başarılı sonuçlar verdiği görülmüştür. Tablonun üst kısmında görünen iki boyutlu matrix incelendiğinde köşegenlerdeki değerler (79, 84, 71, 117, 70) test verilerindeki doğru tahminleri göstermektedir. Sonuçlar önceki eğitimlere göre iyi denilebilecek bir derecededir.

![image](https://user-images.githubusercontent.com/59260491/176998776-a5f4f2ba-1de7-4167-893f-dfe47a1cf229.png)
	
<h5> Şekil 14: MobileNet eğitimden elde edilen confusion matrix </h5>     
	
Önceki haftalarda mobilenet algoritmasından sonraki hedef vgg16 algoritması ile eğitim yapmaktı. Bu hafta vgg16 modelini kullanılarak bir eğitim gerçekleştirildi.
Vgg16 basit bir ağ modeli olup öncesindeki modellerden en önemli farkı evrişim katmanlarının 2’li ya da 3’lü kullanılmasıdır. Tam bağlantı (FC) katmanında 7x7x512=4096 nöronlu bir öznitelik vektörüne dönüştürülür. İki FC katmanı çıkışında 1000 sınıflı softmax başarımı hesaplanır. 

![image](https://user-images.githubusercontent.com/59260491/176998792-fff8eff2-04f1-4a4b-bbe6-8ad91a5ba9df.png)
	
<h5> Şekil 15: VGG16 ağ mimarisi </h5> 
 
![image](https://user-images.githubusercontent.com/59260491/176998827-f463298a-328d-48fa-a938-02f01306dd06.png)
	
<h5> Şekil 16: VGG16 </h5> 
	
VGG16 modelinde eğitimde imagenet ağırlıkları kullanılmıştır. Eğitim 120 epoch olarak gerçekleştirilmiştir. Eğitim sonunda elde edilen f1-score değeri 0.86’dır. Train ve test olarak ayrılan veri seti eğitimden önce x_train, y_train, x_test, y_test olarak ayrılmıştır ve eğitim bu şekilde gerçekleştirilmiştir. Test accuracy değeri 0.75 ve test loss değeri 1.22 olarak elde edilmiştir. Eğitim sonucunda gözlemlemek üzere oluşturulan grafikler ve confusion matrix verilerine göz atalım.
	
![image](https://user-images.githubusercontent.com/59260491/176998850-57d8f824-1e78-4fad-88b8-3547aab0b97c.png)
	
<h5> Şekil 17: 120 epoch sonucu elde edilen değerler </h5> 
	
Grafiklerde görüldüğü üzere validation loss değeri artmıştır. Bunun sebebi eğitimin overfittinge uğraması olarak düşünülmektedir. Önceki eğitimlerde de bu sorunla karşılaşıldığı için epoch sayısının 10 – 15 arasında olmasının en uygun aralık olabileceği düşünüldü. Gelecek hafta epoch sayısı azaltılabildiği kadar azaltılacaktır ve veri setinde uygun görülen bir düzenlemeye gidilecektir.

![image](https://user-images.githubusercontent.com/59260491/176998866-43509d9b-f3bb-4f89-863f-4c2d6f1bc57d.png)
	
<h5> Şekil 18: VGG16 eğitiminden elde edilen confusion matrix </h5> 
	
Confusion matrix verilerine bakıldığında aslında güzel sonuçlar olduğu görülmektedir. Fakat test verilerinde karşılaşılan sınıflandırma hataları tolere edilebilecek bir seviyede değildir. Bu sebepten dolayı modeli iyileştirme çalışmalarına devam edilecek ve validation loss değerinin artması problemine çözüm bulunacaktır.

Bu zamana kadar yapılan tüm eğitimler karşılaştırıldığında vgg16 modelinin eğitiminin mobilenet eğitimden daha iyi olduğu görülmüştür. Veri setinin test bölümünden kendi seçtiğimiz veriler bir liste yardımı ile tahmin edildi. Eğitim sonucunda elde edilen değerlerin yeterliliği değerlendirildi. Overfitting problemi yaşanmaması için eğitim 15 epoch’da tamamlandı. Elde edilen test accuracy değeri 0.754677.

![image](https://user-images.githubusercontent.com/59260491/176998875-dd328e56-0ff3-4092-bcfb-ba6397d56282.png)
	
<h5> Şekil 19:VGG16 eğitiminden elde edilen confusion matrix </h5> 

![image](https://user-images.githubusercontent.com/59260491/176998882-7b377cdb-f3b6-4d82-aec9-b0be6d060622.png)
	
<h5> Şekil 20: VGG ile 15 epoch sonucunda elde edilen loss ve accuracy değerleri </h5> 

Projenin donanım aşamasında elimizde bulunan imkanlar dahilinde beş sınıf ile sınıflandırma yapmak ve bunu uygulamak biraz daha karmaşık ve zor olacağından dolayı projedeki sınıf/kategori sayısı üç sınıf ile sınırlandırıldı. Cam, kağıt ve plastik kategorilerinden oluşan üç sınıf ile vgg16 modeli kullanılarak bir eğitim daha gerçekleştirildi. Hatalı sınıflandırmaların azaldığı görüldü. Üç sınıf ile 50 epoch eğitim yapıldı. Elde edilen test accuracy değeri 0.81.
 
![image](https://user-images.githubusercontent.com/59260491/176998889-4b55c68a-ed18-4d1d-b7b3-7549f49da7e1.png)
	
<h5> Şekil 21: Üç sınıflı VGG16 modelinden elde edilen confusion matrix </h5> 
 
![image](https://user-images.githubusercontent.com/59260491/176998901-8c42b711-8944-482e-8b26-ea1012be65f4.png)
	
<h5> Şekil 22: Eğitim sonucunda elde edilen loss ve accuracy değerleri </h5> 
	
Overfitting sorununa çözüm bulmak amacıyla araştırmalar yapıldı. Araştırmalar sonucunda bulunan çözümler; cnn katmanlarındaki gizli katman sayısını azaltmak, veri artırma, katmanlarda L1 ve L2  normalizasyon işlemi, dropout katmanı eklemek, learning rate oranını azaltmak. Bulunan bu çözümler aşamalı olarak önceki eğitim dosyalarında denendi. Doğruluk değerleri uygun olan modeller üzerinde inceleme yapıldı ve geliştirilmek üzere tekrar eğitimler gerçekleştirildi. Veri artırma işlemi sonucunda her kategorideki verilerin sayısı yaklaşık olarak iki katına çıkarıldı. Veri setindeki görsellerin renk tonları ile oynanarak ve eksenlerini çevirerek çoğaltma yapıldı. Learning rate oranı azaltılarak eğitimin epoch sayısında arttırma işlemi gerçekleştirildi.

![image](https://user-images.githubusercontent.com/59260491/176998907-3ca8df5a-190f-4e04-b77c-31adb82e1f77.png)
	
<h5> Şekil 23: Veri artırırken özelliklerin değiştirilme oranları verildi </h5> 

![image](https://user-images.githubusercontent.com/59260491/176998912-18c82b4e-824e-4da0-9a92-59365dab2541.png)
	
<h5> Şekil 24: Hangi verilere işlem uygulanacağı ve nereye kaydedileceği belirtilip artırma işlemi başlatıldı </h5> 
 
![image](https://user-images.githubusercontent.com/59260491/176998921-9a433242-a63c-4d38-9997-6970ccffab7f.png)
	
<h5> Şekil 25: Learning Rate azaltıldığında eğitimin 60 epoch ile durumu </h5> 
 
![image](https://user-images.githubusercontent.com/59260491/176998936-95938812-444e-4696-9d88-6d7e75a70e63.png)
	
<h5> Şekil 26: Elde edilen test doğruluk değerleri </h5> 


Veri arttırma yönteminden elde edilen verilerin nasıl daha iyi eğitilebileceğine dair üzerinde düşünüldü. Önceki haftalarda yapılan eğitimler incelendi. Eğitimlere yönelik alınan notlar incelendi ve en iyi sonuç veren eğitimlerin farklı parametreler ile tekrar eğitilmesine karar verildi. Önceki eğitimlerde veri setini train ve test olarak ayırma işlemi el ile seçilerek yapılmıştı. Bu işlem yeni eğitimlere geçilmeden önce python kodu ile gerçekleştirildi. Python kodu ile train ve test olarak ayırılan veri seti yeni eğitimler için hazır hale getirildi.
 
![image](https://user-images.githubusercontent.com/59260491/176998949-a206220d-440d-4659-a720-8f2805d9f624.png)
	
<h5> Şekil 27: Train ve test olarak ayırma - Python kodu </h5> 

Önceki haftalarda en iyi eğitim sonucunu veren parametreler kullanılarak veri setinin son hali eğitildi. Eğitimde kullanılan verilerin giriş boyutu 224 olarak ayarlandı. VGG16 algoritması imagenet ağırlıkları ile eğitildi. Eğitim birkaç kez tekrarlandı ve 40 epoch değerinin yeterli olacağı düşünüldü. 

![image](https://user-images.githubusercontent.com/59260491/176998966-e952c998-47e3-45a5-bd59-6d6b5eac4228.png)
	
<h5> Şekil 28: 40 Epoch sonucu elde edilen eğitim verileri </h5> 

![image](https://user-images.githubusercontent.com/59260491/176998972-4216545f-06df-4b44-8fcb-266635d1022d.png)
	
<h5> Şekil 29: 40 epoch sonucu elde edilen eğitim verileri </h5> 

Eğitim sonucunda %90 doğruluk değeri elde edilmiştir. Kayıp değeri ise %26’dır.

 
![image](https://user-images.githubusercontent.com/59260491/176998978-faa08d69-f4a0-4534-b764-e55b77f801b6.png)
	
<h5> Şekil 30: Loss ve accuracy değerleri </h5> 

Son olarak confusion matrix’ten elde edilen değerler incelendiğinde kağıt sınıfı için %96, plastik sınıfı için %85 ve cam sınıfı için %88 f1-score değerleri elde edilmiştir. Doğruluk değerleri de yaklaşık olarak bu değerler ile eşdeğerdir.
	
![image](https://user-images.githubusercontent.com/59260491/176999419-0bf6c0ba-e05e-4b99-8315-d05893cc4dda.png)
	
<h5> Şekil 31: Confusion matrix değerleri ve kod kısmı </h5> 

Elde edilecek sonuçları karşılaştırmak amacıyla veri setindeki görsellerden VGG16 algoritması ile öznitelik çıkarımı yapıldı. Öznitelik çıkarımı yapılan veriler SVM(Support Vector Machine) algoritması ile eğitildi ve elde edilen değerler gözlemlendi.

![image](https://user-images.githubusercontent.com/59260491/176999428-77adcb66-8607-4547-8aca-5294bd1ca915.png)
	
<h5> Şekil 32: SVM ile gerçekleştirilen eğitim </h5> 

Öznitelik çıkarımı VGG16 ile yapılan eğitimde yaklaşık olarak %74 doğruluk elde edildi.

![image](https://user-images.githubusercontent.com/59260491/176999434-fe570629-ffd0-4057-a532-89c1461cd70f.png)
	
<h5> Şekil 33: Eğitim sonucunda elde edilen doğruluk değeri </h5> 
	
Confusion matrix değerleri incelendiğinde VGG16 ile yapılan eğitim değerlerinin daha başarılı olduğu görülmüştür. 
 
![image](https://user-images.githubusercontent.com/59260491/176999439-b194df54-fbd5-45d3-bebb-b722a50ebd75.png)
	
<h5> Şekil 34: SVM eğitimi confusion matrix değerleri </h5> 

Hem öznitelik çıkarımının hem de eğitimin VGG16 algoritması ile gerçekleştirilmesinin daha başarılı sonuçlar ortaya çıkardığı görülmüştür. Bu nedenden dolayı VGG16 algoritması ile son yapılan eğitimimiz projenin en başarılı eğitimi olarak kabul edilmiştir ve donanım testleri bu eğitim sonucunda ortaya çıkan ağırlık dosyası ile gerçekleştirilecektir.

Eğitilen modelin farklı donanımlar üzerinde çalışmasını gözlemlemek için Nvidia Jetson Nano geliştirme kartı üzerinde çalışılmaya başlandı. Jetson Nano, Linux sistemi tarafından desteklenmektedir. Kart üzerine takılan sd kart içine Jetpack ile Jetson Nano için kurulum yapılmaktadır. SD kart üzerine yapılan yazma işlemi genel bir bilgisayarda yapılmaktadır. Genel bilgisayarın işletim sistemi önemli değildir.

![image](https://user-images.githubusercontent.com/59260491/176999444-e24f6698-9e0a-4abe-972c-76bb799e5c70.png)
	
<h5> Şekil 35: Nvidia Jetson Nano Geliştirici Kartı </h5> 

Jetson Nano kartına Jetpack ile birlikte TensorRT, Linux, cuDNN, Cuda, güvenlik, geliştirici araçları, bilgisayarlı görü destekleri sağlanmaktadır. 



Eğitim sonucunda elde edilen model dosyasının testi için Python programlama dilinde yazılmış bir script kullanılacaktır. Test aşamasını gerçekleştirmek için Jetson Nano içinde OpenCV, Keras, Tensorflow kütüphaneleri bulunmalıdır. Keras ve Tensorflow kütüphaneleri eğitilen model dosyasının okunmasını sağlayacaktır. OpenCV kütüphanesi ile test için ayrılan görseller üzerinde işlemler yapılacaktır ve sonucun ekranda görünmesi sağlanacaktır. Gerekli kütüphaneler için kurulum gerçekleştirilmiştir. Şekil 36’da Keras kütüphanesinin Jetson Nano üzerinde kurulum aşaması bulunmaktadır.

![image](https://user-images.githubusercontent.com/59260491/176999452-8680532b-0778-43f1-9755-b463ada03fdb.png)
	
<h5> Şekil 36: Keras kütüphanesi kurulumu </h5> 


OpenCV kütüphanesinin kurulumundan sonra kütüphanenin donanım üzerindeki özellikleri Şekil 37 ve Şekil 38’de incelenmiştir.
	
![image](https://user-images.githubusercontent.com/59260491/176999468-6f30e666-5c48-4654-a4da-59ad8a8d5e50.png)
	
<h5> Şekil 37: OpenCV kütüphanesi özellikleri </h5> 

![image](https://user-images.githubusercontent.com/59260491/176999487-20a509fe-457e-44c6-9076-eb26fb9d4741.png)
	
<h5> Şekil 38: OpenCV kütüphanesi özellikleri </h5> 


Kullanılan Jetson Nano donanımı ve çalışma ortamı Şekil 39’da gösterilmiştir.
  
![image](https://user-images.githubusercontent.com/59260491/176999503-3b69dcfe-5d81-4819-a66f-5a74f81187a2.png)
	
<h5> Şekil 39: Kullanılan donanım Jetson Nano </h5> 


Kütüphane kurulumları gerçekleştirildikten sonra test aşamasına geçilmiştir. Test için ayrılmış veriler ile test işlemleri gerçekleştirilmiştir ve bazıları incelenmek üzere görselleştirilmiştir. Görselleştirilen test verileri ve kodun çalışma aşamasını inceleyelim. 


 ![image](https://user-images.githubusercontent.com/59260491/176999516-97605f8b-5ee2-4cfc-afa0-6ac262bfe3f7.png)
	
<h5> Şekil 40: Test kodunun çalışma aşaması ve kod </h5> 


<h2>  SONUÇLAR </h2> 
 
![image](https://user-images.githubusercontent.com/59260491/176999524-05271b5b-4a6b-49c4-98b2-74d6da60fff1.png)
	 
<h5> Şekil 41: Test sonucunda elde edilen veriler </h5> 

