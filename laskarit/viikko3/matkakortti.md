```mermaid
sequenceDiagram
    main->>laitehallinto: HKLLaitehallinto() 
    main->>rautatietori: Lataajalaite()
    main->>ratikka6: Lukijalaite()
    main->>bussi244: Lukijalaite()
    
    main->>hkl: lisaa_lataaja(rautatietori)
    
    main->>hkl: lisaa_lukija(ratikka6)
    
    main->> hkl: lisaa_lukija(bussi244)

    main->>lippu_luukku: Kioski()
    main ->> lippu_luukku: osta_matkakortti("Kalle")
    activate lippu_luukku
    lippu_luukku ->> kallen_kortti: Matkakortti("Kalle")
    lippu_luukku ->> main: kallen_kortti
    deactivate lippu_luukku
    
    main->>rautatietori : lataa_arvoa(kallen_kortti, 3)
    activate rautatietori
    rautatietori->>kallen_kortti: kasvata_arvoa(3)
    kallen_kortti -->> rautatietori
    deactivate kallen_kortti
    rautatietori -->> main
    deactivate rautatietori
    
   	main ->> ratikka6: osta_lippu(kallen_kortti, 0)
   	activate ratikka6
   	ratikka6 ->> kallen_kortti: kortti.arvo
   	activate kallen_kortti
   	kallen_kortti -->> ratikka6: 3
   	deactivate kallen_kortti
   	ratikka6 ->> kallen_kortti: vahenna_arvoa(1.5)
   	activate kallen_kortti
   	kallen_kortti -->> ratikka6
   	deactivate kallen_kortti
   	ratikka6 ->> main: true
   	deactivate ratikka6
   	
   	main ->> bussi244: osta_lippu(kallen_kortti, 2)
   	activate bussi244
   	bussi224 ->> kallen_kortti: kortti.arvo
   	activate kallen_kortti
   	kallen_kortti -->> bussi244: 1.5
   	deactivate kallen_kortti
   	bussi244 ->> main: false
   	deactivate bussi244
```