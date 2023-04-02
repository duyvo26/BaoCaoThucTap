from django.urls import path, include
import CodeThucTap.views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("login", CodeThucTap.views.Login, name='Login'),
    path("LoginPost", CodeThucTap.views.Login_POST, name='Login_POST'),
    # home du doan mo hinh va cai dat
    path("", CodeThucTap.views.load, name='load'),
    path("home", CodeThucTap.views.index, name='home'),


    path("setting", CodeThucTap.views.setting, name='setting'),

    path("caidat", CodeThucTap.views.caidat, name='caidat'),

    path("setting_POST", CodeThucTap.views.setting_POST, name='setting_POST'),


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



    path("One/GiaiThuatCoDien_POST", CodeThucTap.views.One_GiaiThuatCoDien_POST,
         name='One_GiaiThuatCoDien_POST'),
    #     Two file


]
