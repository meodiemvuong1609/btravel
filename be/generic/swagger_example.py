from drf_yasg import openapi

"""
    ACCOUNT
"""

#swagger login
api_login = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties= {
        "phone"    : openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="1234567890"),
        "password" : openapi.Schema(type=openapi.TYPE_STRING, description="password", default="12345678"),
        "system_code" : openapi.Schema(type=openapi.TYPE_STRING, description="system_code", default="ADMIN"),
    }
)


#swagger forgot password
api_forgot_password = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "phone"   : openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="0346525843"),
        "system_code" : openapi.Schema(type=openapi.TYPE_STRING, description="system_code", default="Admin"),
    }
)

#swagger verify_otp_forgot
verify_otp_forgot = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "otp_forgot"   : openapi.Schema(type=openapi.TYPE_STRING, description="otp_forgot", default="12354"),
        "session_key" : openapi.Schema(type=openapi.TYPE_STRING, description="session_key", default="asfafgdagafa21021"),
    }
)

#swagger reset_password 
api_reset_password = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "session_key" : openapi.Schema(type=openapi.TYPE_STRING, description="session_key", default="asfafgdagafa21021"),
        "new_password" : openapi.Schema(type=openapi.TYPE_STRING, description="new_password", default="123545678"),
        "confirm_password" : openapi.Schema(type=openapi.TYPE_STRING, description="confirm_password", default="123545678"),
    }
)

admin_update_password = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "new_password" : openapi.Schema(type=openapi.TYPE_STRING, description="new_password", default="123545678"),
        "confirm_password" : openapi.Schema(type=openapi.TYPE_STRING, description="confirm_password", default="123545678"),
    }
)

#swagger change_password 
api_change_password = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "old_password" : openapi.Schema(type=openapi.TYPE_STRING, description="old_password", default="123545678"),
        "new_password" : openapi.Schema(type=openapi.TYPE_STRING, description="new_password", default="123545678"),
    }
)

#swagger check_password 
api_check_password = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "password" : openapi.Schema(type=openapi.TYPE_STRING, description="check password correct", default="123545678"),
    }
)

#swagger reset_otp
api_reset_OTP = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "session_key" : openapi.Schema(type=openapi.TYPE_STRING, description="session_key", default="sdfsd65456463sdgsds"),
    }
)

#swagger api_register
api_chth_register = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "account" : openapi.Schema(type=openapi.TYPE_OBJECT, description="campaign",
            properties= {
                "phone" : openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="12354567890"),
                "password" : openapi.Schema(type=openapi.TYPE_STRING, description="password", default="12354789"),
                "full_name" : openapi.Schema(type=openapi.TYPE_STRING, description="password", default="Nguyen Van A"),
            }  
        ),
        "address" : openapi.Schema(type=openapi.TYPE_OBJECT, description="address", 
                properties= {
                    "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="ha noi"),
                    "lat" : openapi.Schema(type=openapi.TYPE_STRING, description="lat", default="11.22"),
                    "long" : openapi.Schema(type=openapi.TYPE_STRING, description="long", default="11.22"),
                    "province": openapi.Schema(type=openapi.TYPE_INTEGER, description="province", default=1),
                    "district": openapi.Schema(type=openapi.TYPE_INTEGER, description="district", default=1),
                    "ward": openapi.Schema(type=openapi.TYPE_INTEGER, description="ward", default=1),
                }), 
        "shop" : openapi.Schema(type=openapi.TYPE_OBJECT, description="shop", 
            properties= {
                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="test"),
                "website" : openapi.Schema(type=openapi.TYPE_STRING, description="website", default="https://api.mykiot.com/swagger/"),
            }   
        ),                          
    }
)

put_detail_account = (
    openapi.Schema(
    openapi.Parameter("id", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    type = openapi.TYPE_OBJECT,    
    properties= {
        "account" : openapi.Schema(type=openapi.TYPE_OBJECT, description="campaign",
            properties= {
                "email" : openapi.Schema(type=openapi.TYPE_STRING, description="email", default="A@idtinc.co"),
                "full_name" : openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
                "referral_code_point" :  openapi.Schema(type=openapi.TYPE_STRING, description="referral_code", default="as45fas4g"),
            }  
        ),
        "address" : openapi.Schema(type=openapi.TYPE_OBJECT, description="address", 
            properties= {
                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="ha noi"),
                "lat" : openapi.Schema(type=openapi.TYPE_STRING, description="lat", default="11.22"),
                "long" : openapi.Schema(type=openapi.TYPE_STRING, description="long", default="11.22"),
                "province": openapi.Schema(type=openapi.TYPE_INTEGER, description="province", default=1),
                "district": openapi.Schema(type=openapi.TYPE_INTEGER, description="district", default=1),
                "ward": openapi.Schema(type=openapi.TYPE_INTEGER, description="ward", default=1),
            }),  

        "bank" : openapi.Schema(type=openapi.TYPE_OBJECT, description="bank", 
            properties= {
                "card_number" : openapi.Schema(type=openapi.TYPE_STRING, description="card_number", default="147258369"),
                "full_name": openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
                "card_type" : openapi.Schema(type=openapi.TYPE_STRING, description="card_type", default=""),
                "bank" : openapi.Schema(type=openapi.TYPE_INTEGER, description="bank", default=1),
            }   
        ),  
        "shop" : openapi.Schema(type=openapi.TYPE_OBJECT, description="shop",
            properties= {      
                "bussiness_type" : openapi.Schema(type=openapi.TYPE_INTEGER, description="bussiness_type", default=1),
                "settings" : openapi.Schema(type=openapi.TYPE_OBJECT, description="shop",
                    properties= {
                        "contact" : openapi.Schema(type=openapi.TYPE_STRING, description="contact", default="Nguyen Van B"),
                        "open_time" : openapi.Schema(type=openapi.TYPE_STRING, description="open_time", default="06:00"),
                        "close_time" : openapi.Schema(type=openapi.TYPE_STRING, description="close_time", default="00:00"),
            })
            }              
        ),                     
    }
)
) 

admin_create_ncc = openapi.Schema(
    type = openapi.TYPE_OBJECT,    
    properties= {
        "file_contract" : openapi.Schema(type=openapi.TYPE_FILE, description="file_contract", default=["File_contract in formdata"]),
        "data": openapi.Schema(type=openapi.TYPE_OBJECT, description="campaign",
            properties= {
        "account" : openapi.Schema(type=openapi.TYPE_OBJECT, description="campaign",
            properties= {
                "email" : openapi.Schema(type=openapi.TYPE_STRING, description="email", default="A@idtinc.co"),
                "full_name" : openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
                "phone": openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="123456789"),
                "password": openapi.Schema(type=openapi.TYPE_STRING, description="password", default="12345678"),
                "account_type": openapi.Schema(type=openapi.TYPE_INTEGER, description="account_type", default=1),
                "settings" : openapi.Schema(type=openapi.TYPE_OBJECT, description="settings", 
                        properties= {
                            "NCC" : openapi.Schema(type=openapi.TYPE_OBJECT, description="settings", 
                                properties={
                                    "title" : openapi.Schema(type=openapi.TYPE_OBJECT, description="title", default="Nguyen Van C"),
                                }
                        ) 
                    }),
            }  
        ),
        "address" : openapi.Schema(type=openapi.TYPE_OBJECT, description="address", 
            properties= {
                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="ha noi"),
                "lat" : openapi.Schema(type=openapi.TYPE_STRING, description="lat", default="11.22"),
                "long" : openapi.Schema(type=openapi.TYPE_STRING, description="long", default="11.22"),
                "province": openapi.Schema(type=openapi.TYPE_INTEGER, description="province", default=1),
                "district": openapi.Schema(type=openapi.TYPE_INTEGER, description="district", default=1),
                "ward": openapi.Schema(type=openapi.TYPE_INTEGER, description="ward", default=1),
            }),  
        "card" : openapi.Schema(type=openapi.TYPE_OBJECT, description="card", 
            properties= {
                "card_number" : openapi.Schema(type=openapi.TYPE_STRING, description="card_number", default="147258369"),
                "full_name": openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
                "card_type" : openapi.Schema(type=openapi.TYPE_INTEGER, description="card_type", default=1),
                "bank" : openapi.Schema(type=openapi.TYPE_INTEGER, description="bank", default=1),
            }   
        ),
    })}
)

admin_create_npt = openapi.Schema(
    type = openapi.TYPE_OBJECT,  
    properties= { 
    "file_contract" : openapi.Schema(type=openapi.TYPE_FILE, description="file_contract", default=["File_contract in formdata"]),
    "data": openapi.Schema(type=openapi.TYPE_OBJECT, description="campaign",
        properties= {
            "account" : openapi.Schema(type=openapi.TYPE_OBJECT, description="campaign",
                properties= {
                    "email" : openapi.Schema(type=openapi.TYPE_STRING, description="email", default="A@idtinc.co"),
                    "full_name" : openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
                    "phone": openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="123456789"),
                    "password": openapi.Schema(type=openapi.TYPE_STRING, description="password", default="12345678"),
                    "business_type": openapi.Schema(type=openapi.TYPE_INTEGER, description="business_type", default=1),
                    "settings" : openapi.Schema(type=openapi.TYPE_OBJECT, description="settings", 
                        properties= {
                            "NPT" : openapi.Schema(type=openapi.TYPE_OBJECT, description="settings", 
                                properties={
                                    "title" : openapi.Schema(type=openapi.TYPE_OBJECT, description="title", default="Nguyen Van C"),
                                }
                        ) 
                    }),
                }  
            ),
            "address" : openapi.Schema(type=openapi.TYPE_OBJECT, description="address", 
                properties= {
                    "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="ha noi"),
                    "lat" : openapi.Schema(type=openapi.TYPE_STRING, description="lat", default="11.22"),
                    "long" : openapi.Schema(type=openapi.TYPE_STRING, description="long", default="11.22"),
                    "province": openapi.Schema(type=openapi.TYPE_INTEGER, description="province", default=1),
                    "district": openapi.Schema(type=openapi.TYPE_INTEGER, description="district", default=1),
                    "ward": openapi.Schema(type=openapi.TYPE_INTEGER, description="ward", default=1),                
                    })}),  
            "card" : openapi.Schema(type=openapi.TYPE_OBJECT, description="card", 
                properties= {
                    "card_number" : openapi.Schema(type=openapi.TYPE_STRING, description="card_number", default="147258369"),
                    "full_name": openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
                    "card_type" : openapi.Schema(type=openapi.TYPE_INTEGER, description="card_type", default=1),
                    "bank" : openapi.Schema(type=openapi.TYPE_INTEGER, description="bank", default=1),
                }   
            ),
            "warehouse" : openapi.Schema(type=openapi.TYPE_OBJECT, description="address", 
                properties= {
                    "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="kHO A"),
                    "status" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status", default=True),
                    "settings" : openapi.Schema(type=openapi.TYPE_OBJECT, description="address",
                        properties={
                            "capacity" : openapi.Schema(type=openapi.TYPE_STRING, description="capacity", default="500 m^3"),
                        }
            )}
            ) ,
            "address_warehouse" : openapi.Schema(type=openapi.TYPE_OBJECT, description="address", 
                properties= {
                    "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="TP Nam Định"),
                    "lat" : openapi.Schema(type=openapi.TYPE_STRING, description="lat", default="11.22"),
                    "long" : openapi.Schema(type=openapi.TYPE_STRING, description="long", default="11.22"),
                    "province": openapi.Schema(type=openapi.TYPE_INTEGER, description="province", default=1),
                    "district": openapi.Schema(type=openapi.TYPE_INTEGER, description="district", default=1),
                    "ward": openapi.Schema(type=openapi.TYPE_INTEGER, description="ward", default=1),
                    }),
    })


api_admin_create_employee = openapi.Schema(
    type = openapi.TYPE_OBJECT,    
    properties= {
        "account" : openapi.Schema(type=openapi.TYPE_OBJECT, description="campaign",
            properties= {
                "email" : openapi.Schema(type=openapi.TYPE_STRING, description="email", default="A@idtinc.co"),
                "full_name" : openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
                "phone": openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="1234567890"),
                "password": openapi.Schema(type=openapi.TYPE_STRING, description="password", default="12345678"),
                "account_type": openapi.Schema(type=openapi.TYPE_INTEGER, description="account_type", default=1)
            }  
        ),
        "address" : openapi.Schema(type=openapi.TYPE_OBJECT, description="address", 
            properties= {
                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="ha noi"),
                "lat" : openapi.Schema(type=openapi.TYPE_STRING, description="lat", default="11.22"),
                "long" : openapi.Schema(type=openapi.TYPE_STRING, description="long", default="11.22"),
                "province": openapi.Schema(type=openapi.TYPE_INTEGER, description="province", default=1),
                "district": openapi.Schema(type=openapi.TYPE_INTEGER, description="district", default=1),
                "ward": openapi.Schema(type=openapi.TYPE_INTEGER, description="ward", default=1),
                }),  
        "card" : openapi.Schema(type=openapi.TYPE_OBJECT, description="card", 
            properties= {
                "card_number" : openapi.Schema(type=openapi.TYPE_STRING, description="card_number", default="147258369"),
                "full_name": openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
                "card_type" : openapi.Schema(type=openapi.TYPE_INTEGER, description="card_type", default=1),
                "bank" : openapi.Schema(type=openapi.TYPE_INTEGER, description="bank", default=1),
            }   
        ),
    }
)


api_admin_npt_create_employee = openapi.Schema(
    type = openapi.TYPE_OBJECT,    
    properties= {
        "avatar" : openapi.Schema(type=openapi.TYPE_FILE, description="avatar", default=["ImageField in formdata"]),
        "data" : openapi.Schema(type=openapi.TYPE_OBJECT, description="data", 
            properties={                   
                "account" : openapi.Schema(type=openapi.TYPE_OBJECT, description="account",
                    properties= {
                        "email" : openapi.Schema(type=openapi.TYPE_STRING, description="email", default="A@idtinc.co"),
                        "full_name" : openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
                        "phone": openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="123456789"),
                        "password": openapi.Schema(type=openapi.TYPE_STRING, description="password", default="123456789"),
                        "account_type": openapi.Schema(type=openapi.TYPE_INTEGER, description="account_type", default=1),
                    }),      
                "address" : openapi.Schema(type=openapi.TYPE_OBJECT, description="address", 
                    properties= {
                        "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="ha noi"),
                        "lat" : openapi.Schema(type=openapi.TYPE_STRING, description="lat", default="11.22"),
                        "long" : openapi.Schema(type=openapi.TYPE_STRING, description="long", default="11.22"),
                        "province": openapi.Schema(type=openapi.TYPE_INTEGER, description="province", default=1),
                        "district": openapi.Schema(type=openapi.TYPE_INTEGER, description="district", default=1),
                        "ward": openapi.Schema(type=openapi.TYPE_INTEGER, description="ward", default=1),
                })})})


put_detail_employee = (
    openapi.Schema(
    type = openapi.TYPE_OBJECT,    
    properties= {      
        "full_name" : openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
        "phone" : openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="1234567890"),
        "email" : openapi.Schema(type=openapi.TYPE_STRING, description="email", default="test@gmail.com"),
        "address" : openapi.Schema(type=openapi.TYPE_INTEGER, description="address", default=1),
        "account_type" : openapi.Schema(type=openapi.TYPE_INTEGER, description="account_type", default= 1),
        "avatar" : openapi.Schema(type=openapi.TYPE_FILE, description="avatar", default=["ImageField in formdata"]),
    }
)
)

put_update_account = (
    openapi.Schema(
    type = openapi.TYPE_OBJECT,    
    properties={                   
                "account" : openapi.Schema(type=openapi.TYPE_OBJECT, description="account",
                    properties= {
                        "email" : openapi.Schema(type=openapi.TYPE_STRING, description="email", default="A@idtinc.co"),
                        "full_name" : openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
                        "phone": openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="123456789"),
                        "settings" : openapi.Schema(type=openapi.TYPE_OBJECT, description="settings", 
                            properties= {
                                "NPT" : openapi.Schema(type=openapi.TYPE_OBJECT, description="settings", 
                                    properties={
                                        "title" : openapi.Schema(type=openapi.TYPE_OBJECT, description="title", default="Nguyen Van C"),
                                    }
                            ) 
                        }),
                        "account_type": openapi.Schema(type=openapi.TYPE_INTEGER, description="account_type", default=1),
                        "business_type": openapi.Schema(type=openapi.TYPE_INTEGER, description="bussiness_type", default=1),

                    }),      
                "warehouse_address" : openapi.Schema(type=openapi.TYPE_OBJECT, description="address", 
                    properties= {
                        "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="ha noi"),
                        "lat" : openapi.Schema(type=openapi.TYPE_STRING, description="lat", default="11.22"),
                        "long" : openapi.Schema(type=openapi.TYPE_STRING, description="long", default="11.22"),
                        "province": openapi.Schema(type=openapi.TYPE_INTEGER, description="province", default=1),
                        "district": openapi.Schema(type=openapi.TYPE_INTEGER, description="district", default=1),
                        "ward": openapi.Schema(type=openapi.TYPE_INTEGER, description="ward", default=1),
                })}
)
)

put_status_account = (
    openapi.Schema(
    type = openapi.TYPE_OBJECT,    
    properties= {      
        "status" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status", default=True),
        "list_account" : openapi.Schema(type=openapi.TYPE_STRING, description="list_account", default=[1, 2]),
    }
)
)

"""
    ACCOUNT_TYPE

"""

post_accounttype = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="Quản lý"),
        "description": openapi.Schema(type=openapi.TYPE_STRING, description="description", default="Mô tả"),
        "settings" : openapi.Schema(type=openapi.TYPE_STRING, description="settings"),
        "account_type_parent" : openapi.Schema(type=openapi.TYPE_INTEGER, description="account_type_parent", default=1),
    }
)

put_detail_accounttype = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="Quản lý"),
        "description": openapi.Schema(type=openapi.TYPE_STRING, description="description", default="Mô tả"),
        "settings" : openapi.Schema(type=openapi.TYPE_STRING, description="settings"),
        "account_type_parent" : openapi.Schema(type=openapi.TYPE_INTEGER, description="account_type_parent", default=1),
    }
)

"""
    CUSTOMER

"""

post_customer = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "customer" : openapi.Schema(type=openapi.TYPE_OBJECT, description="campaign",
            properties= {
                "phone" : openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="12354567890"),
                "email" : openapi.Schema(type=openapi.TYPE_STRING, description="email", default="12354789"),
                "birthday" : openapi.Schema(type=openapi.TYPE_STRING, description="password", default="2023-02-01"),
                "image" : openapi.Schema(type=openapi.TYPE_FILE, description="image", default="link image"),
                "gender" : openapi.Schema(type=openapi.TYPE_STRING, description="gender", default="Nguyen Van A"),
            }  
        ),
        "address" : openapi.Schema(type=openapi.TYPE_OBJECT, description="address", 
                properties= {
                    "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="ha noi"),
                    "lat" : openapi.Schema(type=openapi.TYPE_STRING, description="lat", default="11.22"),
                    "long" : openapi.Schema(type=openapi.TYPE_STRING, description="long", default="11.22"),
                    "province": openapi.Schema(type=openapi.TYPE_INTEGER, description="province", default=1),
                    "district": openapi.Schema(type=openapi.TYPE_INTEGER, description="district", default=1),
                    "ward": openapi.Schema(type=openapi.TYPE_INTEGER, description="ward", default=1),
                })}
)

put_info_account = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "account" : openapi.Schema(type=openapi.TYPE_OBJECT, description="campaign",
            properties= {
                 "settings" : openapi.Schema(type=openapi.TYPE_OBJECT, description="settings", 
                        properties= {
                            "NPT" : openapi.Schema(type=openapi.TYPE_OBJECT, description="settings", 
                                properties={
                                    "name" : openapi.Schema(type=openapi.TYPE_OBJECT, description="title", default="Nguyen Van C"),
                                }
                        ) 
                    }),
                "email" : openapi.Schema(type=openapi.TYPE_STRING, description="email", default="A@gmail.com"),
                "full_name" : openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="12354567890"),
            }  
        ),  
        "address" : openapi.Schema(type=openapi.TYPE_OBJECT, description="address", 
            properties= {
                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="ha noi"),
                "lat" : openapi.Schema(type=openapi.TYPE_STRING, description="lat", default="11.22"),
                "long" : openapi.Schema(type=openapi.TYPE_STRING, description="long", default="11.22"),
                "province": openapi.Schema(type=openapi.TYPE_INTEGER, description="province", default=1),
                "district": openapi.Schema(type=openapi.TYPE_INTEGER, description="district", default=1),
                "ward": openapi.Schema(type=openapi.TYPE_INTEGER, description="ward", default=1),
            }),
        "card" : openapi.Schema(type=openapi.TYPE_OBJECT, description="card", 
                properties= {
                    "card_number" : openapi.Schema(type=openapi.TYPE_STRING, description="card_number", default="147258369"),
                    "full_name": openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
                    "card_type" : openapi.Schema(type=openapi.TYPE_INTEGER, description="card_type", default=1),
                    "bank" : openapi.Schema(type=openapi.TYPE_INTEGER, description="bank", default=1),
                }   
            ),               
})

put_detail_customer = (
    openapi.Schema(
    type = openapi.TYPE_OBJECT,    
    properties= {      
        "full_name" : openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
        "phone" : openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="1234567890"),
        "email" : openapi.Schema(type=openapi.TYPE_STRING, description="email", default="test@gmail.com"),
        "address" : openapi.Schema(type=openapi.TYPE_STRING, description="address", default="Hà Nội"),
        "birthday" : openapi.Schema(type=openapi.TYPE_STRING, description="birthday", default="2023-02-01"),
        "image" : openapi.Schema(type=openapi.TYPE_FILE, description="image", default="link image"),
        "gender" : openapi.Schema(type=openapi.TYPE_INTEGER, description="1 : Nam, 2 : Nữ, 3 : Không xác định", default=1),
    }
)
)

api_create_chth = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "account" : openapi.Schema(type=openapi.TYPE_OBJECT, description="campaign",
            properties= {
                "phone" : openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="12354567890"),
                "password" : openapi.Schema(type=openapi.TYPE_STRING, description="password", default="123545678"),
                "email" : openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="12354567890"),
                "full_name" : openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="12354567890"),
                "referral_code_point" : openapi.Schema(type=openapi.TYPE_STRING, description="key_account", default="1as45afva"),
            }  
        ),
        "shop" : openapi.Schema(type=openapi.TYPE_OBJECT, description="shop", 
            properties= {
                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="test"),
                "website" : openapi.Schema(type=openapi.TYPE_STRING, description="website", default="https://api.mykiot.com/swagger/"),
                "bussiness_type" : openapi.Schema(type=openapi.TYPE_INTEGER, description="bussiness_type", default=1),
                "description" : openapi.Schema(type=openapi.TYPE_STRING, description="description", default="This Shop is..."),
                "settings" : openapi.Schema(type=openapi.TYPE_OBJECT, description="shop",
                    properties= {
                        "contact" : openapi.Schema(type=openapi.TYPE_STRING, description="contact", default="Nguyen Van B"),
                        "open_time" : openapi.Schema(type=openapi.TYPE_STRING, description="open_time", default="06:00"),
                        "close_time" : openapi.Schema(type=openapi.TYPE_STRING, description="close_time", default="00:00"),
            })}   
        ),  
        "address" : openapi.Schema(type=openapi.TYPE_OBJECT, description="address", 
            properties= {
                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="ha noi"),
                "lat" : openapi.Schema(type=openapi.TYPE_STRING, description="lat", default="11.22"),
                "long" : openapi.Schema(type=openapi.TYPE_STRING, description="long", default="11.22"),
                "province": openapi.Schema(type=openapi.TYPE_INTEGER, description="province", default=1),
                "district": openapi.Schema(type=openapi.TYPE_INTEGER, description="district", default=1),
                "ward": openapi.Schema(type=openapi.TYPE_INTEGER, description="ward", default=1),
            }),
        "card" : openapi.Schema(type=openapi.TYPE_OBJECT, description="card", 
                properties= {
                    "card_number" : openapi.Schema(type=openapi.TYPE_STRING, description="card_number", default="147258369"),
                    "full_name": openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
                    "card_type" : openapi.Schema(type=openapi.TYPE_INTEGER, description="card_type", default=1),
                    "bank" : openapi.Schema(type=openapi.TYPE_INTEGER, description="bank", default=1),
                }   
            ),  
        "warehouse" : openapi.Schema(type=openapi.TYPE_OBJECT, description="address", 
            properties= {
                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="kHO A"),
                "status" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status", default=True),
            } 
        )             
}
)

"""
    CARD

"""

post_card = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "card_number" : openapi.Schema(type=openapi.TYPE_STRING, description="card_number", default="147258369"),
        "full_name": openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
        "status" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status: default=True", default=True),
        "qrcode" : openapi.Schema(type=openapi.TYPE_FILE, description="qrcode"),
        "cvv" : openapi.Schema(type=openapi.TYPE_STRING, description="cvv", default="123"),
        "expriry_date" : openapi.Schema(type=openapi.TYPE_STRING, description="expriry_date", default="01/02"),
        "card_type" : openapi.Schema(type=openapi.TYPE_INTEGER, description="card_type, example: 1", default=1),
        "bank" : openapi.Schema(type=openapi.TYPE_INTEGER, description="bank, example: 1", default=1),
    }
)

put_detail_card = (
    openapi.Schema(
    type = openapi.TYPE_OBJECT,    
    properties= {      
        "card_number" : openapi.Schema(type=openapi.TYPE_STRING, description="card_number", default="147258369"),
        "full_name": openapi.Schema(type=openapi.TYPE_STRING, description="full_name", default="Nguyen Van A"),
        "status" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status: default=True", default=True),
        "qrcode" : openapi.Schema(type=openapi.TYPE_FILE, description="qrcode"),
        "cvv" : openapi.Schema(type=openapi.TYPE_STRING, description="cvv", default="123"),
        "expriry_date" : openapi.Schema(type=openapi.TYPE_STRING, description="expriry_date", default="01/02"),
        "card_type" : openapi.Schema(type=openapi.TYPE_INTEGER, description="card_type, example: 1", default=1),
        "bank" : openapi.Schema(type=openapi.TYPE_INTEGER, description="bank, example: 1", default=1),
    }
)
)

"""
    ADDRESS

"""

put_detail_address = (
    openapi.Schema(
    type = openapi.TYPE_OBJECT,    
    properties= {
                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="ha noi"),
                "lat" : openapi.Schema(type=openapi.TYPE_STRING, description="lat", default="11.22"),
                "long" : openapi.Schema(type=openapi.TYPE_STRING, description="long", default="11.22"),
                "province": openapi.Schema(type=openapi.TYPE_INTEGER, description="province", default=1),
                "district": openapi.Schema(type=openapi.TYPE_INTEGER, description="district", default=1),
                "ward": openapi.Schema(type=openapi.TYPE_INTEGER, description="ward", default=1),
            }
)
)

"""
    ORDER

"""

post_order = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "order" : openapi.Schema(type=openapi.TYPE_OBJECT, description="full_name",
            properties= {
                'title' : openapi.Schema(type=openapi.TYPE_STRING, description='phone'),
                'discount' : openapi.Schema(type=openapi.TYPE_STRING, description='discount', default="10000"),
                'customer' : openapi.Schema(type=openapi.TYPE_INTEGER, description='customer: 1', default=1),
                "is_online" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description='default=True', default=True),
                "note" : openapi.Schema(type=openapi.TYPE_STRING, description='note', default="abc"),
        }),
        "orderitem" : openapi.Schema(type=openapi.TYPE_ARRAY, description="orderitem",
            items= openapi.Schema(type=openapi.TYPE_OBJECT, description="item",
            properties = {
                "quantity" : openapi.Schema(type=openapi.TYPE_INTEGER, description="quantity", default=100),
                "price" : openapi.Schema(type=openapi.TYPE_NUMBER, description="price", default="100000"),
                "discount" : openapi.Schema(type=openapi.TYPE_NUMBER, description="discount", default="20000"),
                "variant" : openapi.Schema(type=openapi.TYPE_INTEGER, description="variant", default=1),
            }))}
)

put_detail_order = openapi.Schema(
    type = openapi.TYPE_OBJECT,    
    properties= {
        "status" : openapi.Schema(type=openapi.TYPE_INTEGER, description="status : 1", default=1),
        "note" : openapi.Schema(type=openapi.TYPE_STRING, description="note", default="abc"),
    }
)

put_status_ordersystem = (
    openapi.Schema(
    type = openapi.TYPE_OBJECT,    
    properties= {      
        'status' : openapi.Schema(type=openapi.TYPE_STRING, description='status', default= 5),
    }
)
)

put_status_order = (
    openapi.Schema(
    type = openapi.TYPE_OBJECT,    
    properties= {      
        "status" : openapi.Schema(type=openapi.TYPE_STRING, description="status", default= 5),
    }
)
)

"""
    BRAND

"""

post_brand = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "media" : openapi.Schema(type=openapi.TYPE_FILE, description="media", default=["ImageField in formdata"]),
        "data": openapi.Schema(type=openapi.TYPE_OBJECT, description="data", 
            properties={
                "brand" :  openapi.Schema(type=openapi.TYPE_OBJECT, description="product",
                    properties={
                        "title": openapi.Schema(type=openapi.TYPE_STRING, description="title", default="thuong hieu A"),
                    }),
                "product" : openapi.Schema(type=openapi.TYPE_NUMBER, description="product", default=[1,2]),
                "product_brand": openapi.Schema(type=openapi.TYPE_ARRAY, description="product", 
                    items = openapi.Schema(type=openapi.TYPE_OBJECT, description="product", 
                        properties={
                            "product": openapi.Schema(type=openapi.TYPE_OBJECT, description="product_id", default=1),
                            "brand" : openapi.Schema(type=openapi.TYPE_OBJECT, description="brand_id", default=2),
                        }
                )),
            })
    }
)


put_detail_brand = (
    openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "media" : openapi.Schema(type=openapi.TYPE_STRING, description="media", default=['form data image']),
        "data" : openapi.Schema(type=openapi.TYPE_OBJECT, description="data", 
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING, description="title", default="thuong hieu A"),
                "product" : openapi.Schema(type=openapi.TYPE_ARRAY, description="list variants", default=[1, 2],
                    items= openapi.Schema(type=openapi.TYPE_INTEGER, description="variant ID"))
            }                                                  
        ),
    }
)
)

"""
    PRODUCT_GROUP

"""

post_productgroup = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties={
        "productgroup": openapi.Schema(type=openapi.TYPE_OBJECT, description="group name",
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING, description="title"),
                "product" : openapi.Schema(type=openapi.TYPE_NUMBER, description="product id",default=[1,2])
            }),
        "productcategory" : openapi.Schema(type=openapi.TYPE_NUMBER, description="product id",default=1),
        "product_group": openapi.Schema(type=openapi.TYPE_ARRAY, description="product", 
                    items = openapi.Schema(type=openapi.TYPE_OBJECT, description="product", 
                        properties={
                            "product": openapi.Schema(type=openapi.TYPE_OBJECT, description="product_id", default=1),
                            "group" : openapi.Schema(type=openapi.TYPE_OBJECT, description="brand_id", default=2),
                        }
                )),
    }
)


put_detail_productgroup = (
    openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="test1"),
        "product" : openapi.Schema(type=openapi.TYPE_NUMBER, description="product id",default=[1,2]),
        "product_category": openapi.Schema(type=openapi.TYPE_NUMBER, description="product_category id",default=1),
    }
)
)

"""
    PRODUCT_CATEGORY

"""

post_productcategory = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='title'),
            'product' : openapi.Schema(type=openapi.TYPE_STRING, description='new product group',default=[1,2]),
            'group' : openapi.Schema(type=openapi.TYPE_STRING, description='new product group',default=[1,2])
        }
)


put_detail_productcategory = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='title'),
            'product' : openapi.Schema(type=openapi.TYPE_STRING, description='new product group',default=[1,2]),
            'group' : openapi.Schema(type=openapi.TYPE_STRING, description='new product group',default=[1,2])
        }
)

#swagger create porduct
api_create_product = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "media_product" : openapi.Schema(type=openapi.TYPE_ARRAY, description="media product",
            items=openapi.Schema(type=openapi.TYPE_FILE, description="Array image field"), default=["ImageField in formdata"]),
        "media_variant" : openapi.Schema(type=openapi.TYPE_ARRAY, description="media variant",
            items=openapi.Schema(type=openapi.TYPE_FILE, description="Array image field"), default=["ImageField in formdata"]),
        "data": openapi.Schema(type=openapi.TYPE_OBJECT, description="data",
            properties={
                "product": openapi.Schema(type=openapi.TYPE_OBJECT, description="product",
                properties={
                    "title": openapi.Schema(type=openapi.TYPE_STRING, description="product title", default="testabc"),
                    "barcode": openapi.Schema(type=openapi.TYPE_STRING, description="barcode", default="1146"),
                    "price_sell": openapi.Schema(type=openapi.TYPE_NUMBER, description="product sell price", default=5000),
                    "price_import": openapi.Schema(type=openapi.TYPE_NUMBER, description="price_import", default=4000),
                    "status_product": openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status_product", default=True),
                    "status_online": openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status_online", default=True),
                    "description": openapi.Schema(type=openapi.TYPE_STRING, description="description", default="san pham ..."),
                    "settings": openapi.Schema(type=openapi.TYPE_ARRAY, description="settings",
                        items= openapi.Schema(type=openapi.TYPE_OBJECT, description="item",
                            properties={
                                "title": openapi.Schema(type=openapi.TYPE_STRING, description="title", default="Mau sac"),
                                "value": openapi.Schema(type=openapi.TYPE_ARRAY, description="value", default=["red", "blue"], items=openapi.Schema(type=openapi.TYPE_STRING)),
                        })),
                }
            ),
                "variant" : openapi.Schema(type=openapi.TYPE_ARRAY, description="new product variant", 
                    items= openapi.Schema(type=openapi.TYPE_OBJECT, description="item",
                    properties={
                        "title": openapi.Schema(type=openapi.TYPE_STRING, description="product title", default="testabc"),
                        "barcode": openapi.Schema(type=openapi.TYPE_STRING, description="barcode", default="64654"),
                        "price_sell": openapi.Schema(type=openapi.TYPE_NUMBER, description="product sell price", default=10000),
                        "price_import": openapi.Schema(type=openapi.TYPE_NUMBER, description="price_import", default=10000),
                        "status" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status", default=True),
                        "quantity" : openapi.Schema(type=openapi.TYPE_NUMBER, description="quantity", default=100),
                        "options" : openapi.Schema(type=openapi.TYPE_ARRAY, description="options",
                            items= openapi.Schema(type=openapi.TYPE_OBJECT, description="item",
                            properties={
                                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="vị"),
                                "values" : openapi.Schema(type=openapi.TYPE_STRING, description="values", default="ngọt"),
                                "status" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status", default=True),
                            }))
                    }
                )),
                'brand' : openapi.Schema(type=openapi.TYPE_INTEGER, description='brand', default=1),
                'productgroup' : openapi.Schema(type=openapi.TYPE_INTEGER, description='productgroup', default=1),
                'productcategory' : openapi.Schema(type=openapi.TYPE_INTEGER, description='productcategory', default=1),
                'list_media_variant' : openapi.Schema(type=openapi.TYPE_STRING, description='new product variant', default=[True, False]),
                }
            )})


api_update_product = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "media_product" : openapi.Schema(type=openapi.TYPE_ARRAY, description="media product",
            items=openapi.Schema(type=openapi.TYPE_FILE, description="Array image field"), default=["ImageField in formdata"]),
        "media_variant" : openapi.Schema(type=openapi.TYPE_ARRAY, description="media variant",
            items=openapi.Schema(type=openapi.TYPE_FILE, description="Array image field"), default=["ImageField in formdata"]),
        "data": openapi.Schema(type=openapi.TYPE_OBJECT, description="data",
            properties={
                "product": openapi.Schema(type=openapi.TYPE_OBJECT, description="product",
                properties={
                    "title": openapi.Schema(type=openapi.TYPE_STRING, description="product title", default="testabc"),
                    "barcode": openapi.Schema(type=openapi.TYPE_STRING, description="barcode", default="1146"),
                    "price_sell": openapi.Schema(type=openapi.TYPE_NUMBER, description="product sell price", default=5000),
                    "price_import": openapi.Schema(type=openapi.TYPE_NUMBER, description="price_import", default=4000),
                    "status_product": openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status_product", default=True),
                    "status_online": openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status_online", default=True),
                    "description": openapi.Schema(type=openapi.TYPE_STRING, description="description", default="san pham ..."),
                    "media" : openapi.Schema(type=openapi.TYPE_FILE, description="media delete", default=[1,2]),
                    "settings": openapi.Schema(type=openapi.TYPE_ARRAY, description="settings",
                        items= openapi.Schema(type=openapi.TYPE_OBJECT, description="item",
                            properties={
                                "title": openapi.Schema(type=openapi.TYPE_STRING, description="title", default="Mau sac"),
                                "value": openapi.Schema(type=openapi.TYPE_ARRAY, description="value", default=["red", "blue"], items=openapi.Schema(type=openapi.TYPE_STRING)),
                        })),
                    "option" : openapi.Schema(type=openapi.TYPE_STRING, description="option", default="Chọn 1 trong các key: ['ALL', 'NULL', 'SELL', 'IMPORT']"),
                },
                
            ),
                "variant" : openapi.Schema(type=openapi.TYPE_ARRAY, description="new product variant", 
                    items= openapi.Schema(type=openapi.TYPE_OBJECT, description="item",
                    properties={
                        "title": openapi.Schema(type=openapi.TYPE_STRING, description="product title", default="testabc"),
                        "barcode": openapi.Schema(type=openapi.TYPE_STRING, description="barcode", default="64654"),
                        "price_sell": openapi.Schema(type=openapi.TYPE_NUMBER, description="product sell price", default=10000),
                        "price_import": openapi.Schema(type=openapi.TYPE_NUMBER, description="price_import", default=10000),
                        "status" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status", default=True),
                        "quantity" : openapi.Schema(type=openapi.TYPE_NUMBER, description="quantity", default=100),
                        "options" : openapi.Schema(type=openapi.TYPE_ARRAY, description="options",
                            items= openapi.Schema(type=openapi.TYPE_OBJECT, description="item",
                            properties={
                                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="vị"),
                                "values" : openapi.Schema(type=openapi.TYPE_STRING, description="values", default="ngọt"),
                                "status" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status", default=True),
                            }))
                    }
                )),
                'brand' : openapi.Schema(type=openapi.TYPE_INTEGER, description='brand', default=1),
                'productgroup' : openapi.Schema(type=openapi.TYPE_INTEGER, description='productgroup', default=1),
                'productcategory' : openapi.Schema(type=openapi.TYPE_INTEGER, description='productcategory', default=1),
                'list_media_variant' : openapi.Schema(type=openapi.TYPE_STRING, description='new product variant', default=[True, False]),
            }
        )})

# modify product
put_detail_product = (
    openapi.Schema(
        openapi.Parameter("id", openapi.IN_QUERY, type=openapi.TYPE_STRING),
        type=openapi.TYPE_OBJECT,
        properties={
            "title": openapi.Schema(type=openapi.TYPE_STRING, description="product title", default="testabc"),
            "price_sell": openapi.Schema(type=openapi.TYPE_STRING, description="product sell price", default="10000"),
            "price_import": openapi.Schema(type=openapi.TYPE_STRING, description="product import price", default="10000"),
            "system": openapi.Schema(type=openapi.TYPE_INTEGER, description="product system id", default=3),
            "quantity": openapi.Schema(type=openapi.TYPE_NUMBER, description="product quantity", default="100"),
            "barcode": openapi.Schema(type=openapi.TYPE_STRING, description="product barcode", default="test"),
            "brand": openapi.Schema(type=openapi.TYPE_INTEGER, description="product brand", default=1),
        }
    )
)

# create unit
post_unit = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "title": openapi.Schema(type=openapi.TYPE_STRING, description="unit title", default="ten don vi"),
    }
)

# update unit
put_unit = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "title": openapi.Schema(type=openapi.TYPE_STRING, description="unit title", default="ten don vi")
    }
)


"""
    ORDER SYSTEM

"""

post_ordersystem = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "order" : openapi.Schema(type=openapi.TYPE_OBJECT, description="full_name",
            properties= {
                'title' : openapi.Schema(type=openapi.TYPE_STRING, description='title', default="0123456789"),
                'discount' : openapi.Schema(type=openapi.TYPE_STRING, description='discount', default="10000"),
                "note" : openapi.Schema(type=openapi.TYPE_STRING, description='note', default="test"),
                "account_sell" : openapi.Schema(type=openapi.TYPE_INTEGER, description='account_sell: 1', default=1),
        }),
        "orderitem" : openapi.Schema(type=openapi.TYPE_ARRAY, description="orderitem",
            items= openapi.Schema(type=openapi.TYPE_OBJECT, description="item",
            properties = {
                "quantity" : openapi.Schema(type=openapi.TYPE_INTEGER, description="quantity", default=100),
                "price" : openapi.Schema(type=openapi.TYPE_NUMBER, description="price", default=10000),
                "discount" : openapi.Schema(type=openapi.TYPE_NUMBER, description="discount", default=10000),
                "variant" : openapi.Schema(type=openapi.TYPE_INTEGER, description="variant", default=1),
                "promotion" : openapi.Schema(type=openapi.TYPE_INTEGER, description="promotion", default=1),
            }))}
)

put_detail_ordersystem = openapi.Schema(
    type = openapi.TYPE_OBJECT,    
    properties= {
        "account_trans" : openapi.Schema(type=openapi.TYPE_INTEGER, description="account_trans", default=1),
    }
)

put_ordersystem = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "order" : openapi.Schema(type=openapi.TYPE_OBJECT, description="full_name",
            properties= {
                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="order 1"),
                "status" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status", default=False),
                "total" : openapi.Schema(type=openapi.TYPE_STRING, description="total", default="1000"),
                "discount" : openapi.Schema(type=openapi.TYPE_STRING, description="discount", default="20000"),
                "account_buy": openapi.Schema(type=openapi.TYPE_STRING, description="account_buy", default=1),
                "account_sell" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="account_sell", default=1),
                "account_trans" : openapi.Schema(type=openapi.TYPE_STRING, description="account_trans", default=1),
        }),
        "order_item": openapi.Schema(type=openapi.TYPE_OBJECT, 
            properties={
                "delete": openapi.Schema(type=openapi.TYPE_ARRAY, description="delete", default=[1, 2],
                        items=openapi.Schema(type=openapi.TYPE_INTEGER)                    
                    ),
                "create": openapi.Schema(type=openapi.TYPE_ARRAY, description="create",
                        items=openapi.Schema(type=openapi.TYPE_OBJECT,
                        properties={
                            "quantity": openapi.Schema(type=openapi.TYPE_STRING, description="quantity", default=100),
                            "price": openapi.Schema(type=openapi.TYPE_INTEGER, description="price", default=100),
                            "promotion": openapi.Schema(type=openapi.TYPE_INTEGER, description="promotion", default=1),
                            "discount": openapi.Schema(type=openapi.TYPE_INTEGER, description="discount", default=1000),
                            "variant": openapi.Schema(type=openapi.TYPE_INTEGER, description="variant", default=1),
                    }                     
                    )),
                "update" : openapi.Schema(type=openapi.TYPE_ARRAY, description="update",
                        items=openapi.Schema(type=openapi.TYPE_OBJECT,
                        properties={
                            "id": openapi.Schema(type=openapi.TYPE_INTEGER, description="type_location", default=1),
                            "quantity": openapi.Schema(type=openapi.TYPE_STRING, description="quantity", default=100),
                            "price": openapi.Schema(type=openapi.TYPE_INTEGER, description="price", default=100),
                            "promotion": openapi.Schema(type=openapi.TYPE_INTEGER, description="promotion", default=1),
                            "discount": openapi.Schema(type=openapi.TYPE_INTEGER, description="discount", default=1000),
                            "variant": openapi.Schema(type=openapi.TYPE_INTEGER, description="variant", default=1),
                    }                     
                    )),
            }),
    })



api_adminconfirmorder = openapi.Schema(
    type = openapi.TYPE_OBJECT,    
    properties= {
        "account_trans" : openapi.Schema(type=openapi.TYPE_INTEGER, description="account_trans", default=1),
    }
)

"""
    CANCEL ORDER SYSTEM

"""

cancel_ordersystem = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "reason" : openapi.Schema(type=openapi.TYPE_OBJECT, description="Lý do khác (nếu có) sẽ truyền input người dùng nhập. Nếu không có thì không truyền key này",
            properties= {
                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="test"),
        }),
        "cancel_order" : openapi.Schema(type=openapi.TYPE_OBJECT, description="cancel_order",
            properties = {
                "order" : openapi.Schema(type=openapi.TYPE_INTEGER, description="order", default=1),
                "reason" : openapi.Schema(type=openapi.TYPE_INTEGER, description="Lý do sẵn có. Nếu lý do khác thì không truyền key này", default=1),
        })}
)


# create variant
post_variant = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "title": openapi.Schema(type=openapi.TYPE_STRING, description="variant title", default="ten thuoc tinh"),
    }
)

# update unit
put_variant = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "title": openapi.Schema(type=openapi.TYPE_STRING, description="variant title", default="ten thuoc tinh")
    }
)



# create product variant
post_productvariant = openapi.Schema(type=openapi.TYPE_ARRAY, description="new product variant",
    items= openapi.Schema(type=openapi.TYPE_OBJECT, description="product variant item",
    properties={
        "value": openapi.Schema(type=openapi.TYPE_STRING, description="value", default="Red"),
        "variant": openapi.Schema(type=openapi.TYPE_NUMBER, description="Variant id", default=1),
        }
    )
)

#put product variant
put_productvariant = openapi.Schema(type=openapi.TYPE_ARRAY, description="new product variant",
    items= openapi.Schema(type=openapi.TYPE_OBJECT, description="product variant item",
    properties={
            "value": openapi.Schema(type=openapi.TYPE_STRING, description="value", default="Red"),
            "variant": openapi.Schema(type=openapi.TYPE_NUMBER, description="Variant id", default=1),
        }
    )
)

"""
    ORDER SYSTEM ADMIN, NPT

"""

adminnpt_order = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "order" : openapi.Schema(type=openapi.TYPE_OBJECT, description="full_name",
            properties= {
                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="0123456789"),
                "discount" : openapi.Schema(type=openapi.TYPE_STRING, description="discount", default="10000"),
                "status" : openapi.Schema(type=openapi.TYPE_INTEGER, description="status : 1", default=1),
                "is_online" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="default=True", default=True),
                "note" : openapi.Schema(type=openapi.TYPE_STRING, description="note", default="test"),
                "account_buy" : openapi.Schema(type=openapi.TYPE_INTEGER, description="account_buy: 1", default=1),
        }),
        "orderitem" : openapi.Schema(type=openapi.TYPE_ARRAY, description="orderitem",
            items= openapi.Schema(type=openapi.TYPE_OBJECT, description="item",
            properties = {
                "quantity" : openapi.Schema(type=openapi.TYPE_INTEGER, description="quantity", default=100),
                "price" : openapi.Schema(type=openapi.TYPE_NUMBER, description="price", default=10000),
                "discount" : openapi.Schema(type=openapi.TYPE_NUMBER, description="discount", default=10000),
                "variant" : openapi.Schema(type=openapi.TYPE_INTEGER, description="variant", default=1),
            }))}
)


#QR CODE

post_qrcode = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "card": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID Tài khoản", default=1),
    }
)

patch_qrcode = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "status": openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status", default=True),
    }
)

# PROMOTION
post_promotion = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "promotion" : openapi.Schema(type=openapi.TYPE_OBJECT, description="full_name",
            properties= {
                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="0123456789"),
                "status" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status : 1", default=True),
                "code" : openapi.Schema(type=openapi.TYPE_STRING, description="code", default="KHT15SDGD"),
                "type_location": openapi.Schema(type=openapi.TYPE_STRING, description="type_location", default='ALL'),
                "province" : openapi.Schema(type=openapi.TYPE_ARRAY, description="list province", default=[1, 2],
                    items= openapi.Schema(type=openapi.TYPE_INTEGER, description="province ID"),                        
                ),
                "start" : openapi.Schema(type=openapi.TYPE_STRING, description="datetime", default="2023-02-01"),
                "end" : openapi.Schema(type=openapi.TYPE_STRING, description="datetime", default="2023-09-26T23:00:00+07:00"),
        }),
        "location_promotion": openapi.Schema(type=openapi.TYPE_ARRAY, description="location_promotion",
            items=openapi.Schema(type=openapi.TYPE_OBJECT, 
            properties={
                "type_location": openapi.Schema(type=openapi.TYPE_STRING, description="type_location", default='INCLUDE'),
                "area": openapi.Schema(type=openapi.TYPE_INTEGER, description="area", default=1),
                "province" : openapi.Schema(type=openapi.TYPE_ARRAY, description="list province", default=[1, 2],
                    items= openapi.Schema(type=openapi.TYPE_INTEGER, description="province ID"),                        
                ),
            })),
        "promotion_item" : openapi.Schema(type=openapi.TYPE_ARRAY, description="orderitem",
            items= openapi.Schema(type=openapi.TYPE_OBJECT, description="item",
            properties = {
                "quantity" : openapi.Schema(type=openapi.TYPE_INTEGER, description="quantity", default=100),
                "discount" : openapi.Schema(type=openapi.TYPE_NUMBER, description="price", default=10000),
                "type_discount" : openapi.Schema(type=openapi.TYPE_NUMBER, description="type_discount", default=1),
                "variant" : openapi.Schema(type=openapi.TYPE_INTEGER, description="variant", default=1),
                "system" : openapi.Schema(type=openapi.TYPE_ARRAY, description="variant", default=[1, 2],
                    items= openapi.Schema(type=openapi.TYPE_INTEGER, description="item")    
                ),
            }))
        })

put_detail_promotion = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "promotion" : openapi.Schema(type=openapi.TYPE_OBJECT, description="full_name",
            properties= {
                "title" : openapi.Schema(type=openapi.TYPE_STRING, description="phone", default="0123456789"),
                "status" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status", default=False),
                "type_location": openapi.Schema(type=openapi.TYPE_STRING, description="type_location", default='ALL'),
                "status_stop" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status_stop", default=True),
                "province" : openapi.Schema(type=openapi.TYPE_ARRAY, description="list province", default=[1, 2],
                    items= openapi.Schema(type=openapi.TYPE_INTEGER, description="province ID"),                        
                ),
                "start" : openapi.Schema(type=openapi.TYPE_STRING, description="datetime", default="2023-02-01"),
                "end" : openapi.Schema(type=openapi.TYPE_STRING, description="datetime", default="2023-09-26T23:00:00+07:00"),
        }),
        "location": openapi.Schema(type=openapi.TYPE_OBJECT, description="full_name", 
            properties={
                "delete": openapi.Schema(type=openapi.TYPE_ARRAY, description="type_location", default=[1, 2],
                        items=openapi.Schema(type=openapi.TYPE_INTEGER)                    
                    ),
                "create": openapi.Schema(type=openapi.TYPE_ARRAY, description="type_location",
                        items=openapi.Schema(type=openapi.TYPE_OBJECT, description="area",
                        properties={
                            "type_location": openapi.Schema(type=openapi.TYPE_STRING, description="type_location", default='ALL'),
                            "area": openapi.Schema(type=openapi.TYPE_INTEGER, description="area", default=1),
                            "province": openapi.Schema(type=openapi.TYPE_ARRAY, description="type_location", default=[1, 2],
                                items=openapi.Schema(type=openapi.TYPE_INTEGER)                      
                            ),
                    }                     
                    )),
                "update" : openapi.Schema(type=openapi.TYPE_ARRAY, description="type_location",
                        items=openapi.Schema(type=openapi.TYPE_OBJECT, description="area",
                        properties={
                            "id": openapi.Schema(type=openapi.TYPE_INTEGER, description="type_location", default=1),
                            "type_location": openapi.Schema(type=openapi.TYPE_STRING, description="type_location", default='ALL'),
                            "area": openapi.Schema(type=openapi.TYPE_INTEGER, description="area", default=1),
                            "province": openapi.Schema(type=openapi.TYPE_ARRAY, description="type_location", default=[1, 2],
                                items=openapi.Schema(type=openapi.TYPE_INTEGER)                      
                            ),
                    }                     
                    )),
            }),
        "promotion_item" : openapi.Schema(type=openapi.TYPE_OBJECT, description="full_name", 
            properties={
                "delete": openapi.Schema(type=openapi.TYPE_ARRAY, description="type_location", default=[1, 2],
                        items=openapi.Schema(type=openapi.TYPE_INTEGER)                    
                    ),
                "create": openapi.Schema(type=openapi.TYPE_ARRAY, description="type_location",
                        items=openapi.Schema(type=openapi.TYPE_OBJECT, description="area",
                        properties = {
                            "quantity" : openapi.Schema(type=openapi.TYPE_INTEGER, description="quantity", default=100),
                            "discount" : openapi.Schema(type=openapi.TYPE_NUMBER, description="price", default=10000),
                            "type_discount" : openapi.Schema(type=openapi.TYPE_NUMBER, description="type_discount", default=1),
                            "settings": openapi.Schema(type=openapi.TYPE_OBJECT, description="type_discount", default={"ABC" : "abc"}),
                            "variant" : openapi.Schema(type=openapi.TYPE_INTEGER, description="variant", default=1),
                            "system" : openapi.Schema(type=openapi.TYPE_ARRAY, description="variant", default=[1, 2],
                                items= openapi.Schema(type=openapi.TYPE_INTEGER, description="item")    
                            ),
                        }                     
                    )),
                "update" : openapi.Schema(type=openapi.TYPE_ARRAY, description="type_location", 
                        items=openapi.Schema(type=openapi.TYPE_OBJECT, description="area",
                        properties = {
                            "id" : openapi.Schema(type=openapi.TYPE_INTEGER, description="id", default=1),
                            "quantity" : openapi.Schema(type=openapi.TYPE_INTEGER, description="quantity", default=100),
                            "discount" : openapi.Schema(type=openapi.TYPE_NUMBER, description="price", default=10000),
                            "type_discount" : openapi.Schema(type=openapi.TYPE_NUMBER, description="type_discount", default=1),
                            "settings": openapi.Schema(type=openapi.TYPE_OBJECT, description="type_discount", default={"ABC" : "abc"}),
                            "variant" : openapi.Schema(type=openapi.TYPE_INTEGER, description="variant", default=1),
                            "system" : openapi.Schema(type=openapi.TYPE_ARRAY, description="variant", default=[1, 2],
                                items= openapi.Schema(type=openapi.TYPE_INTEGER, description="item")    
                            ),
                        }                   
                    )),
            }),
    })

get_promotion_variant =(openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "variants" : openapi.Schema(type=openapi.TYPE_ARRAY, description="list variants", default=[1, 2],
            items= openapi.Schema(type=openapi.TYPE_INTEGER, description="variant ID"),                        
        ),
    }
)
)

api_update_promotionitem = openapi.Schema(type=openapi.TYPE_OBJECT,
            properties = {
                "quantity" : openapi.Schema(type=openapi.TYPE_INTEGER, description="quantity", default=100),
                "discount" : openapi.Schema(type=openapi.TYPE_NUMBER, description="price", default=10000),
                "type_discount" : openapi.Schema(type=openapi.TYPE_NUMBER, description="type_discount", default=1),
                "variant" : openapi.Schema(type=openapi.TYPE_INTEGER, description="variant", default=1),
                "promotion": openapi.Schema(type=openapi.TYPE_INTEGER, description="promotion", default=1),
            })                
        

# WAREHOUSE

post_warehouse = openapi.Schema(type=openapi.TYPE_ARRAY, description="new product variant",
    items= openapi.Schema(type=openapi.TYPE_OBJECT, description="product variant item",
    properties={
        "title": openapi.Schema(type=openapi.TYPE_STRING, description="value", default="Red"),
        "status": openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status", default=True),
        "warehouse_type": openapi.Schema(type=openapi.TYPE_NUMBER, description="warehouse_type", default=1),
        "address": openapi.Schema(type=openapi.TYPE_NUMBER, description="address", default=1),
        }
    )
)

put_warehouse = openapi.Schema(type=openapi.TYPE_ARRAY, description="new product variant",
    items= openapi.Schema(type=openapi.TYPE_OBJECT, description="product variant item",
    properties={
        "title": openapi.Schema(type=openapi.TYPE_STRING, description="value", default="Red"),
        "status": openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status", default=True),
        "warehouse_type": openapi.Schema(type=openapi.TYPE_NUMBER, description="warehouse_type", default=1),
        "address": openapi.Schema(type=openapi.TYPE_NUMBER, description="address", default=1),
        }
    )
)

get_warehouse_account = ( openapi.Schema(type = openapi.TYPE_OBJECT,
    properties= {
        "account" : openapi.Schema(type=openapi.TYPE_INTEGER, description="account", default=1),
    }
)
)


# VARIANT

put_detail_variant = (
    openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "image": openapi.Schema(type=openapi.TYPE_FILE, description="image", default="ImageField in formdata"),
        "data": openapi.Schema(type=openapi.TYPE_OBJECT, description="data",
            properties={
                "barcode" : openapi.Schema(type=openapi.TYPE_STRING, description="barcode", default="1236874678678"),
                "price_sell" : openapi.Schema(type=openapi.TYPE_NUMBER, description="price_sell", default=3000.0),
                "price_import" : openapi.Schema(type=openapi.TYPE_NUMBER, description="price_import",default=2000.0),
                "quantity" : openapi.Schema(type=openapi.TYPE_INTEGER, description="quantity", default=100),
                "status" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="status", default=True),
            })
    }
)
)

check_atm_card = (
    openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "bin": openapi.Schema(type=openapi.TYPE_STRING, description="bin", default="123456"),
        "accountNumber": openapi.Schema(type=openapi.TYPE_STRING, description="accountNumber", default="123456"),
        "transferType": openapi.Schema(type=openapi.TYPE_STRING, description="INHOUSE is MB, NAPAS for diff", default="INHOUSE"),
    }
)
)

variant_account_detail = (
    openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "account": openapi.Schema(type=openapi.TYPE_STRING, description="account", default=1),
        "variant": openapi.Schema(type=openapi.TYPE_STRING, description="variant", default=2),
    }
)
)

variant_account_list = (
    openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "account": openapi.Schema(type=openapi.TYPE_STRING, description="account", default=1),
        "page" : openapi.Schema(type=openapi.TYPE_STRING, description="page", default=1),
        "limit" : openapi.Schema(type=openapi.TYPE_STRING, description="limit", default=20),
    }
)
)

"""
    CONTRACT

"""

post_contract = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="Nguyen Van A"),
        "file" : openapi.Schema(type=openapi.TYPE_FILE, description="file", default=["Form data"]),
        "account" : openapi.Schema(type=openapi.TYPE_INTEGER, description="account", default=1),
    }
)

put_detail_contract = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "title" : openapi.Schema(type=openapi.TYPE_STRING, description="title", default="Nguyen Van A"),
        "file" : openapi.Schema(type=openapi.TYPE_FILE, description="file", default=["Form data"]),
        "account" : openapi.Schema(type=openapi.TYPE_INTEGER, description="account", default=1),
    }
)

'''
    NOTIFY

'''

put_notify = openapi.Schema(
    type = openapi.TYPE_OBJECT,
    properties= {
        "is_read" : openapi.Schema(type=openapi.TYPE_BOOLEAN, description="is_read", default=True),
    }
)