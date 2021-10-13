from django.shortcuts import get_list_or_404, get_object_or_404 
from django.http import HttpResponse, JsonResponse
from .models import User, Project
from .serializers import ProjectSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import json



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request, email):
    user = get_object_or_404(User, email=email)
    return HttpResponse(json.dumps(user.get_dashboard()), content_type='application/json')



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def project_detail(_, project_id):

      """
      Get all information for a single project.
      """

      route = get_object_or_404(Project, pk=project_id)
      serializer = ProjectSerializer(route, many=False)
      return JsonResponse(serializer.data, safe=False)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):

      serializer = ProjectSerializer(data=request.data)

      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['UPDATE'])
@permission_classes([IsAuthenticated])
def update_project(request):

      existing_project = get_object_or_404(Project, pk=request.data['project_id'])
      serializer = ProjectSerializer(existing_project, data=request.data)

      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_projects(_, company):

      """
      Get all information for a single project.
      """

      projects = get_list_or_404(Project, company=company)
      serializer = ProjectSerializer(projects, many=True)
      return JsonResponse(serializer.data, safe=False)