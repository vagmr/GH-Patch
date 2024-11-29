init python:

    import re
    def replace_text(t):
        ### Chinese
        if _preferences.language == "vagmrts":
            t = t.replace("Allison" , "艾莉森")
            t = t.replace("Amelia" , "阿米莉亚")
            t = t.replace("Elizabeth" , "伊丽莎白")
            t = t.replace("Catherine" , "凯瑟琳")
            t = t.replace("Shawna" , "肖娜")
            t = t.replace("Aaliyah" , "阿丽雅")
            t = t.replace("Shizuka" , "静香")
            t = t.replace("Aiko" , "爱子")
            t = t.replace("Jamila" , "贾米拉")
            t = t.replace("Betty" , "贝蒂")
            t = t.replace("Omar" , "奥马尔")
            t = t.replace("Fiona" , "菲欧娜")
            t = t.replace("Sophia" , "索菲亚")
            t = t.replace("Tanya" , "坦尼娅")
            t = t.replace("Priya" , "普里亚")
            t = t.replace("Elaine" , "伊莱恩")
            t = t.replace("Karen" , "凯伦")
            t = t.replace("Mabel" , "梅布尔")
            t = t.replace("Sister Maria" , "玛丽亚修女")
            t = t.replace("Mila" , "米拉")
            t = t.replace("Jada" , "贾达")
            t = t.replace("Father Peters" , "彼得斯神父")
            t = t.replace("Svetlana" , "斯韦特兰娜")
            t = t.replace("Lina" , "丽娜")
            t = t.replace("Natalia" , "娜塔莉亚")
            t = t.replace("Polly" , "波利")
            t = t.replace("Sandra" , "桑德拉")
            t = t.replace("Jerome" , "杰罗姆")
            t = t.replace("Riona" , "里奥纳")
            t = t.replace("Isabella" , "伊莎贝拉")
            t = t.replace("Asami" , "麻美")
            t = t.replace("Ophelia" , "奥菲莉亚")
            t = t.replace("Paveena" , "帕韦纳")
            t = t.replace("Lily" , "莉莉")
            t = t.replace("Petunia" , "佩妮")
            t = t.replace("Twins" , "双胞胎")
            t = t.replace("Ella" , "埃拉")
            t = t.replace("Ellie" , "艾莉")
            t = t.replace("Zelda" , "塞尔达")
            t = t.replace("Josianne" , "乔西安")
            t = t.replace("Minnie" , "米妮")
            t = t.replace("Molly" , "莫莉")
            t = t.replace("Annabelle" , "安娜贝尔")
            t = t.replace("Jasmine" , "茉莉")
            t = t.replace("Brandi" , "布兰迪")
            t = t.replace("Marcel" , "马塞尔")
            t = t.replace("Williams" , "威廉姆斯")
            t = t.replace("Missus" , "太太")
            t = t.replace("Miller" , "米勒")

#########

            t = t.replace("Monkey" , "猴")
            t = t.replace("Zeus" , "宙斯")
            t = t.replace("Pet" , "宠物")
            t = t.replace("Daddy" , "爸爸")
            t = t.replace("DADDY" , "爸爸")
            t = t.replace("Puppy" , "小狗")
            t = t.replace("Piggy" , "小猪")
            t = t.replace("Piglet" , "小猪仔")
            t = t.replace("Mommy" , "妈咪")

            t = t.replace("Both" , "两者")
            t = t.replace("Woman" , "女人")
            t = t.replace("Relationships" , "关系")
            t = t.replace("Gallery" , "画廊")
            t = t.replace("Main" , "主")

            t = t.replace("Both" , "两者")
            t = t.replace("Officer" , "警官")
            t = t.replace("Policewoman" , "女警察")
            t = t.replace("Megan" , "梅根")
            t = t.replace("Nurse" , "护士")
            t = t.replace("Cashier" , "收银员")
            t = t.replace("Everyone" , "每个人")
            t = t.replace("Man" , "男人")
            t = t.replace("Phone" , "手机")

            t = t.replace("Sir" , "先生")

#########
            t = t.replace("Night" , "夜晚")
            t = t.replace("Morning" , "上午")
            t = t.replace("Evening" , "傍晚")
           
#########我的
            t = t.replace("GH-About" , "版本说明")
            t = t.replace("afdian" , "爱发电")
            t = t.replace("Name: " , "姓名：")
            ## 关系界面的名字
            t = t.replace("Amy" , "艾米")
            t = t.replace("Liz" , "莉兹")
            t = t.replace("Cat" , "凯特")
            t = t.replace("Maria" , "玛丽亚")
            t = t.replace("Veena" , "帕韦纳")



        return t
    config.replace_text = replace_text
