from django.urls import path, include
import mOC_iSVM.views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
     
     # home du doan mo hinh va cai dat
    path("", mOC_iSVM.views.load, name='load'),
    path("home", mOC_iSVM.views.index, name='home'),
    
    
    path("setting", mOC_iSVM.views.setting, name='setting'),
    
    path("caidat", mOC_iSVM.views.caidat, name='caidat'),
    
    path("setting_POST", mOC_iSVM.views.setting_POST, name='setting_POST'),
    
    
    path("showData", mOC_iSVM.views.showData, name='showData'),
    path("listModel", mOC_iSVM.views.listModel,
            name='listModel'),
    path("DowMOdel", mOC_iSVM.views.DowMOdel,
            name='DowMOdel'),
    # end home du doan mo hinh va cai dat
    
#     Chuan doan
    path("ChuanDoanPost", mOC_iSVM.views.ChuanDoan,
         name='ChuanDoanPost'),
    
# end chuan doan
    
    # not scenario
    # one file
#     File/GiaiThuatCoDien
    path("One/GiaiThuatCoDien", mOC_iSVM.views.One_GiaiThuatCoDien,
         name='One_GiaiThuatCoDien'),
    
    path("GiaiThuatCoDien_Show", mOC_iSVM.views.GiaiThuatCoDien_Show,
         name='GiaiThuatCoDien_Show'),
    
    
    
    path("One/GiaiThuatCoDien_POST", mOC_iSVM.views.One_GiaiThuatCoDien_POST,
         name='One_GiaiThuatCoDien_POST'),
    #     Two file
 

]
