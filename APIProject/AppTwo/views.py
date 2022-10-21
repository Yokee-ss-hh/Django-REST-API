from . models import StudentModel
from . serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

print("--------------------------------------API View -----------------------------------")


class StudentDataView(APIView):

    def get(self, request):
        students = StudentModel.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDataViewDetail(APIView):

    def get(self,request, pk):
        students = StudentModel.objects.get(pk=pk)
        serializer = StudentSerializer(students)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        student = StudentModel.objects.get(pk=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        student = StudentModel.objects.get(pk=pk)
        serializer = StudentSerializer(instance=student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = StudentModel.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


print("--------------------------------------Generic API View -----------------------------------")
