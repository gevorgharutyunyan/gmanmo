from django.urls import path
from budget.statistic import Statistics
from budget.views import SpentCreate, SpentList, SpentLoginView, RegisterPage, EditSpent, SpentDelete, MainMenu
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('spent', SpentList.as_view(), name="spent"),
    path('logout', LogoutView.as_view(next_page="login"), name="logout"),
    path('spent-update/<int:pk>/', EditSpent.as_view(), name="spent-update"),
    path('spent-delete/<int:pk>/', SpentDelete.as_view(), name="spent-delete"),
    path('', SpentLoginView.as_view(), name="login"),
    path('stat', Statistics.render_statistic, name="stat"),
    path('main-menu', MainMenu.as_view(), name="main-menu"),
    path('register', RegisterPage.as_view(), name="register"),
    path('spent-create/', SpentCreate.as_view(), name="spent-create"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
