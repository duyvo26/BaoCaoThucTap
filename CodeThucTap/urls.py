from django.urls import path, include
import CodeThucTap.views
from django.conf.urls.static import static
from django.conf import settings
import CodeThucTap.mOC_iSVM

urlpatterns = [
    path("login", CodeThucTap.views.Login, name='Login'),
    path("LoginPost", CodeThucTap.views.Login_POST, name='Login_POST'),
    # home du doan mo hinh va cai dat
    path("", CodeThucTap.views.load, name='load'),
    path("home", CodeThucTap.views.index, name='home'),


    path("setting", CodeThucTap.views.setting, name='setting'),

    path("caidat", CodeThucTap.views.caidat, name='caidat'),

    path("setting_POST", CodeThucTap.views.setting_POST, name='setting_POST'),
    path("settingStyle_POST", CodeThucTap.views.settingStyle_POST,
         name='settingStyle_POST'),
    path("settingModel_POST", CodeThucTap.views.settingModel_POST,
         name='settingModel_POST'),
    
    path("LoadCookie", CodeThucTap.views.LoadCookie,
         name='LoadCookie'),
    

    path("showData", CodeThucTap.views.showData, name='showData'),
    path("listModel", CodeThucTap.views.listModel,
         name='listModel'),
    path("DowMOdel", CodeThucTap.views.DowMOdel,
         name='DowMOdel'),
    # end home du doan mo hinh va cai dat

    #     Chuan doan
    path("ChuanDoanPost", CodeThucTap.views.ChuanDoan,
         name='ChuanDoanPost'),

    # end chuan doan

    path("GiaiThuatCoDien_Show", CodeThucTap.views.GiaiThuatCoDien_Show,
         name='GiaiThuatCoDien_Show'),
    
    path("GiaiThuatCoDien_POST", CodeThucTap.views.GiaiThuatCoDien_POST,
         name='GiaiThuatCoDien_POST'),
    
    
    # mOC_iSVM
    # tim nu gamma
     path("FindBestNG", CodeThucTap.mOC_iSVM.FindNuGamma, name='FindNuGamma'),
     
     
    path("FindNuGamma_POST", CodeThucTap.mOC_iSVM.FindNuGamma_POST,
         name='FindNuGamma_POST'),
    
    
#     mOC_iSVM_AP
#    AP
    path("mOC_iSVM/AP", CodeThucTap.mOC_iSVM.One_mOC_iSVM_AP, name='One_mOC_iSVM_AP'),
    path("mOC_iSVM/AP_POST", CodeThucTap.mOC_iSVM.One_mOC_iSVM_AP_POST,
         name='One_mOC_iSVM_AP_POST'),
#     nB
    path("mOC_iSVM/nB", CodeThucTap.mOC_iSVM.One_mOC_iSVM_nB,
         name='One_mOC_iSVM_nB'),
    path("mOC_iSVM/nB_POST", CodeThucTap.mOC_iSVM.One_mOC_iSVM_nB_POST,
         name='One_mOC_iSVM_nB_POST'),
    
    #  EP
    path("mOC_iSVM/EP", CodeThucTap.mOC_iSVM.One_mOC_iSVM_EP,
         name='One_mOC_iSVM_EP'),
    path("mOC_iSVM/EP_POST", CodeThucTap.mOC_iSVM.One_mOC_iSVM_EP_POST,
         name='One_mOC_iSVM_EP_POST'),
]
