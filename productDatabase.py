
import layoutFunction

treeFrame = layoutFunction.layoutF('Tree','acting_artifical_logo.png',True,200)

laptopFrame = layoutFunction.layoutF('Laptop','acting_artifical_logo.png',False,5000000)

beeFrame = layoutFunction.layoutF('Bee','acting_artifical_logo.png',True,3400)

waterBottleFrame = layoutFunction.layoutF('Water Bottle','acting_artifical_logo.png',False,4300)

wildflowerFrame = layoutFunction.layoutF('Wildflower seed','acting_artifical_logo.png',True,100)

earbudsFrame = layoutFunction.layoutF('Earpods','acting_artifical_logo.png',False,79000)

teddyFrame = layoutFunction.layoutF('Teddy bear','acting_artifical_logo.png',False,1000)

stickerFrame = layoutFunction.layoutF('Sticker','acting_artifical_logo.png',False,50)

voucher50Frame = layoutFunction.layoutF('50p Voucher','acting_artifical_logo.png',False,500)

voucher100Frame = layoutFunction.layoutF('£1 Voucher','acting_artifical_logo.png',False,1000)

voucher200Frame = layoutFunction.layoutF('£2 Voucher','acting_artifical_logo.png',False,2000)

product_layout = [
    [treeFrame, laptopFrame, beeFrame],
    [waterBottleFrame, wildflowerFrame, earbudsFrame],
    [teddyFrame, stickerFrame, voucher50Frame],
    [voucher100Frame, voucher200Frame]
]

product_list = []

for list in product_layout:
    for element in list:
        product_list.append(element)

def key_list():
    for element in product_list


