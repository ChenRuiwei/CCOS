from models import *

newAdministrator = Administrator("admin", "123456", "18271910086")
newAdministrator.save()

canteen1 = Canteen(administrator=newAdministrator,
                   canteen_name="一食堂",
                   location="荔园四栋楼下",
                   photo_url="https://www.google.com/url?sa=i&url=https%3A%2F%2F699pic.com%2Ftupian%2Fshitang.html"
                             "&psig=AOvVaw1myhr6g2ionRNV1C9Atbxs&ust=1698765961904000&source=images&cd=vfe&opi"
                             "=89978449&ved=0CBEQjRxqFwoTCOjgoL-KnoIDFQAAAAAdAAAAABAE")

canteen2 = Canteen(administrator=newAdministrator,
                   canteen_name="二食堂",
                   location="荔园二栋对面",
                   photo_url="https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg95.699pic.com%2Fphoto%2F50077"
                             "%2F0213.jpg_wh300.jpg&tbnid=MZ0gpjOp6rHJIM&vet=12ahUKEwiLwP"
                             "--ip6CAxWf6DgGHWBZBFEQMygFegQIARBU..i&imgrefurl=https%3A%2F%2F699pic.com%2Ftupian"
                             "%2Fshitang.html&docid=4ILuij1TPnAMKM&w=450&h=300&q=%E9%A3%9F%E5%A0%82%E5%9B%BE%E7%89%87"
                             "&ved=2ahUKEwiLwP--ip6CAxWf6DgGHWBZBFEQMygFegQIARBU")

canteen3 = Canteen(administrator=newAdministrator,
                   canteen_name="三食堂",
                   location="荔园七栋楼下",
                   photo_url="https://www.google.com/url?sa=i&url=https%3A%2F%2F699pic.com%2Ftupian%2Fshitang.html"
                             "&psig=AOvVaw1myhr6g2ionRNV1C9Atbxs&ust=1698765961904000&source=images&cd=vfe&opi"
                             "=89978449&ved=0CBEQjRxqFwoTCOjgoL-KnoIDFQAAAAAdAAAAABAE")

canteen4 = Canteen(administrator=newAdministrator,
                   canteen_name="四食堂",
                   location="荔园十栋对面",
                   photo_url="https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg95.699pic.com%2Fphoto%2F50077"
                             "%2F0213.jpg_wh300.jpg&tbnid=MZ0gpjOp6rHJIM&vet=12ahUKEwiLwP"
                             "--ip6CAxWf6DgGHWBZBFEQMygFegQIARBU..i&imgrefurl=https%3A%2F%2F699pic.com%2Ftupian"
                             "%2Fshitang.html&docid=4ILuij1TPnAMKM&w=450&h=300&q=%E9%A3%9F%E5%A0%82%E5%9B%BE%E7%89%87"
                             "&ved=2ahUKEwiLwP--ip6CAxWf6DgGHWBZBFEQMygFegQIARBU")

canteen1.save()
canteen2.save()
canteen3.save()
canteen4.save()
