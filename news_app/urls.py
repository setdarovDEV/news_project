from django.urls import path
from .views import news_list, news_detail, homePageView, ContactPageView, page404, aboutPage, HomePageView, \
    LocalNewsView, ForiegnNewsView, TexnologyNewsView, SportNewsView, NewsUpdateView, NewsDeleteView, NewsCreateView, \
    admin_page_view, SearchResultsList
urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<slug:news>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('page404/', page404, name='404_page'),
    path('about-us/', aboutPage, name='about_page'),
    path('local/', LocalNewsView.as_view(), name='local_news_page'),
    path('foriegn/', ForiegnNewsView.as_view(), name='foriegn_news_page'),
    path('texnology/', TexnologyNewsView.as_view(), name='texnology_news_page'),
    path('sport/', SportNewsView.as_view(), name='sport_news_page'),
    path('adminpage/', admin_page_view, name='admin_page'),
    path('searchresult/', SearchResultsList.as_view(), name='search_results')
]

