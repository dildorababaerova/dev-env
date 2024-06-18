from django.shortcuts import render

def catalog(request):
    context:dict[str, str] = {
        'title': 'Etusivu-Catalog',
        'goods': [
        {'image': 'deps/images/goods/kuva1.png',
         'name': 'Kukat',
         'description': 'Hienot kukat',
         'price': 150.00},

         {'image': 'deps/images/goods/kuva2.png',
         'name': 'Maljakko',
         'description': 'Tyylikas maljakko',
         'price': 93.00},

         {'image': 'deps/images/goods/kuva3.png',
         'name': 'Enkelit',
         'description': 'Enkelit.',
         'price': 670.00},

         {'image': 'deps/images/goods/kuva5.png',
         'name': 'rasiat',
         'description': 'Hienot rasiat. ',
         'price': 365.00},

         {'image': 'deps/images/goods/kuva4.png',
         'name': 'Kananmunia',
         'description': 'Eri kokoisia kanamunia.',
         'price': 430.00},

         {'image': 'deps/images/goods/kuva6.png',
         'name': 'Kukat',
         'description': 'Hienot kukat.',
         'price': 610.00},

         {'image': 'deps/images/goods/kuva7.png',
         'name': 'Erikoiskukka',
         'description': 'Прикроватный столик с двумя выдвижными ящиками (цветок не входит в комплект).',
         'price': 55.00},

         {'image': 'deps/images/goods/kuva8.png',
         'name': 'Elaimia',
         'description': 'Kilpikonna',
         'price': 190.00},

         {'image': 'deps/images/goods/kuva9.png',
         'name': 'Erikoiskananmunat',
         'description': 'Erillaisia kananmunia',
         'price': 30.00},

         {'image': 'deps/images/goods/kuva10.png',
         'name': 'Elaimia',
         'description': 'Lintujen perhe',
         'price': 10.00},

         {'image': 'deps/images/goods/kuva11.png',
         'name': 'Kukka',
         'description': 'Kukka yksitelleen',
         'price': 15.00},

         {'image': 'deps/images/bg-image.png',
         'name': 'Talot',
         'description': 'Erilaisia taloja',
         'price': 25.00},
        ]
    }
   
    
    return render(request, 'goods/catalog.html', context)


def product(request):
   
    
    return render(request, 'goods/product.html')

