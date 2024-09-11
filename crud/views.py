from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Anime
from .serializer import *
from django.shortcuts import get_object_or_404


# class AnimeView(APIView):
#     queryset = Anime.objects.all()
#     serializer_class = AnimeSerializer

#     def get(self,request):
#         result = Anime.objects.all().values()
#         return Response({'message':'list of animes',"anime list":result})
    
#     def post(self,request):
#         print('Request data is: ',request.data)
#         serializer_obj= AnimeSerializer(data=request.data) 
#         if(serializer_obj.is_valid()):

#             Anime.objects.create(id = serializer_obj.get("id"),
#                                  name = serializer_obj.get("name"),
#                                  character = serializer_obj.get("character"),
#                                  role = serializer_obj.get("role"),
#                                  )
#         anime = Anime.objects.all().get(id=request.data["id"]).values()
#         return Response({'message':'New anime added',"anime":anime})
    

class GetAnime(APIView):
    def get(self, request):
        var = Anime.objects.all()
        serializer = AnimeSerializer(var, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "msg": "Your data is added",
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED,
                }
            )
        return Response(
            {
                "msg": "Your data is added",
                "error": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST,
            }
        )
    
    def patch(self,request):
            var = Anime.objects.get(id=request.data.get('id'))
            serializer = AnimeSerializer(var,data=request.data,partial=True)
            if serializer.is_valid():
                 serializer.save()
                 return Response({"msg":"updated",
                                  "data":serializer.data,
                                  "status":"succes",
            }
        )
            else:
                 return Response({"msg":"updated",
                                  "data":serializer.errors,
                                  "status":"error",
            }
        )
    
    def put(self,request):
            var = Anime.objects.get(id=request.data.get('id'))
            serializer = AnimeSerializer(var,data=request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response({"msg":"updated",
                                  "data":serializer.data,
                                  "status":"succes",
            }
        )
            else:
                 return Response({"msg":"updated",
                                  "data":serializer.errors,
                                  "status":"error",
            }
        )
        
    def delete(self,request,id=None):
         var = get_object_or_404(Anime,id=request.data.get('id'))
         var.delete()
         return Response({"msg":"deleted",
                          "data":"record deleted",
                          })

