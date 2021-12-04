import json
userlogin_dict_ashok={
    "username":"ashok",
    "userId":12,
    "type":"user",
    "token":{"Auth":True,"type":"user"}
    }
providerlogin_dict_siva={
    "username":"siva",
    "userId":102,
    "type":"provider",
    "token":{"Auth":True,"type":"provider"}
    }
main_services_dict=[{
    "Electrial":{
        "CardTitle":"Electrial Services",
        "CardDiscription":"1.Electrial maintanance works..., 2.Electrial Installation works... 3.Electrial Repair works...", 
        "image":"https://i.pinimg.com/originals/f6/87/3c/f6873c84de97a3d997032922cbcce66f.jpg"  
    },
    "Plumbing":{
        "CardTitle":"Plumbing Services",
        "CardDiscription":"1.Electrial maintanance works..., 2.Electrial Installation works... 3.Electrial Repair works...", 
        "image":"https://www.callks.com/wp-content/uploads/2019/08/ks-services-plumbing-how-a-home-plumbing-system-works-1024x534.jpg"  
    },
    "Painting":{
        "CardTitle":"Painting Services",
        "CardDiscription":"1.Painting maintanance works..., 2.Painting Installation works... 3.Painting Repair works...",  
        "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzqc4R27utlRsziV9Lj0S9qcHWY3WXuFvICHZYJUbzx7DvAhcgv-6DoykrCIbTxZmUOUU&usqp=CAU" 
    },
    "Carpentry":{
        "CardTitle":"Carpentry Services",
        "CardDiscription":"1.Carpentry maintanance works..., 2.Carpentry Installation works... 3.Carpentry Repair works...", 
        "image":"data:image/jpeg;base64,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"  
    }
}]
Sub_services_dict=[{
    "Electrial":{
        "Ac_repair_Works":{
            "title":"AC Repair Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },
         "Ac_Installation_Works":{
            "title":"AC Installation Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },
          "Ac_Maintanance_Works":{
            "title":"AC Maintanance Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },
          "Inverter_repair_Works":{
            "title":"Inverter Repair Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },
         "Inverter_Installation_Works":{
            "title":"Inverter Installation Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },
          "Inverter_Maintanance_Works":{
            "title":"Inverter Maintanance Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },
          "WashingMachine_repair_Works":{
            "title":"WashingMachine Repair Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },
         "WashingMachine_Installation_Works":{
            "title":"WashingMachine Installation Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },
          "WashingMachine_Maintanance_Works":{
            "title":"WashingMachine Maintanance Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        }
},
    "Plumbing":{ 
        "Ac_repair_Works":{
            "title":"AC Repair Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },
         "Ac_Installation_Works":{
            "title":"AC Installation Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },
          "Ac_Maintanance_Works":{
            "title":"AC Maintanance Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },
          "Inverter_repair_Works":{
            "title":"Inverter Repair Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },
         "Inverter_Installation_Works":{
            "title":"Inverter Installation Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },
          "Inverter_Maintanance_Works":{
            "title":"Inverter Maintanance Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
         },
},      
    "Carpentry":{
          "WashingMachine_repair_Works":{
            "title":"WashingMachine Repair Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },
         "WashingMachine_Installation_Works":{
            "title":"WashingMachine Installation Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },
          "WashingMachine_Maintanance_Works":{
            "title":"WashingMachine Maintanance Works",
            "Dis":"All Brands Ac's are will get good Repair services,also new equipments will be replaced ",
            "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2tOIdZtOcGEypwHEWZOCkuuI-UFibyeN8Nw&usqp=CAU"
        },   
         
}
}]
def subservices(subservice):
    if(subservice!=""):
        key_dict=subservice
        return json.dumps(Sub_services_dict[f"{key_dict}"]),
        
           
  
