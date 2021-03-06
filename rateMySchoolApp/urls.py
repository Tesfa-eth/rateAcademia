from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='ratemySchool-index'),
    path('collegeRating/', views.college_rating, name='collegeRating'),
    path('professorrating/', views.professor_rating, name='professorrating'),
    path("dashboard/", views.dashboard, name="dashboard"), 
    path("myratings/", views.myRatings, name="myratings"), 
    path('updatePost/<int:pk>/', views.updatePost, name="updatepost"),
    path('updateProfPost/<int:pk>/', views.updateprofpost, name="updateprofpost"),
    path("profile/", views.profile, name="profile"), 
    path("editProfile/", views.editProfile, name="editprofile"), 
    path("accounts/", include("allauth.urls")),
    # admin manage Posts
    path('managePosts/', views.managePosts, name='manageposts'),
    path('manageuser/<int:pk>/', views.manageUserProfile, name='manageuser'),
    path('reportconfirmation/<int:pk>/', views.reportConfirmation, name='reportconfirmation'),
    path('reportprofconfirmation/<int:pk>/', views.reportProfConfirmation, name='reportprofconfirmation'),
    path('postdetail/<int:pk>/', views.postDetail, name='postdetail'),
    path('postprofdetail/<int:pk>/', views.postProfDetail, name='postprofdetail'),
    #path('upvote/<int:pk>/', views.upvote, name='upvote'),
    #path('downvote/<int:pk>/', views.downvote, name='downvote'),
    path('like', views.like, name='like'), # new
    path('dislike', views.dislike, name='dislike'), # new
    path('proflike', views.proflike, name='proflike'), # new
    path('profdislike', views.profdislike, name='profdislike') # new

]