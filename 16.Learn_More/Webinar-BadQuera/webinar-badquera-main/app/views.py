from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import College, Lesson
from app.serializers import CollegeSerializer, LessonSerializer


class LessonView(APIView):

    def get(self, request, lesson_id, *args, **kwargs):
        try:
            lesson = Lesson.objects.get(id=lesson_id)
            if request.user.is_superuser or request.user.userprofile.colleges.filter(id=lesson.college.id).exists():
                serialized_lesson = LessonSerializer(instance=lesson)
                return Response(serialized_lesson.data, status=200)
            else:
                return Response({'errors': ['you are not a member of this college']}, status=403)
        except Lesson.DoesNotExist:
            return Response({'errors': ['no lesson found with this id']}, status=404)

    def put(self, request, lesson_id, *args, **kwargs):
        if request.user.is_superuser:
            try:
                lesson = Lesson.objects.get(id=lesson_id)
                serialized_lesson = CollegeSerializer(instance=lesson, data=request.data)
                if serialized_lesson.is_valid():
                    serialized_lesson.save()
                    return Response(serialized_lesson.data, status=200)
                return Response(serialized_lesson.errors, status=400)
            except Lesson.DoesNotExist:
                return Response({'errors': ['no lesson found with this id']}, status=404)

        return Response({'errors': ['you should be a superuser']}, status=403)


class AllLessonsView(APIView):

    def get(self, request, *args, **kwargs):
        college_id = request.data.get('college_id')
        if college_id:
            if request.user.is_superuser or request.user.userprofile.colleges.filter(id=college_id).exists():
                lessons = Lesson.objects.filter(college__id=college_id)
                serialized_lessons = LessonSerializer(instance=lessons, many=True)
                return Response(serialized_lessons.data)
            else:
                return Response({'errors': ['you are not a member of this college']}, status=403)

        return Response({'errors': ['you should specify college_id']}, status=400)

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            serialized_lessons = LessonSerializer(data=request.data)
            if serialized_lessons.is_valid():
                serialized_lessons.save()
                return Response(serialized_lessons.data, status=201)
            return Response(serialized_lessons.errors, status=400)

        return Response({'errors': ['you should be a superuser']}, status=403)


class CollegeView(APIView):

    def get(self, request, college_id, *args, **kwargs):
        if request.user.is_superuser or request.user.userprofile.colleges.filter(id=college_id).exists():
            try:
                college = College.objects.get(id=college_id)
                serialized_college = CollegeSerializer(instance=college)
                return Response(serialized_college.data, status=200)
            except College.DoesNotExist:
                return Response({'errors': ['no college found with this id']}, status=404)
        else:
            return Response({'errors': ['you are not a member of this college']}, status=403)

    def put(self, request, college_id, *args, **kwargs):
        if request.user.is_superuser:
            try:
                college = College.objects.get(id=college_id)
                serialized_college = CollegeSerializer(instance=college, data=request.data)
                if serialized_college.is_valid():
                    serialized_college.save()
                    return Response(serialized_college.data, status=200)
                return Response(serialized_college.errors, status=400)
            except College.DoesNotExist:
                return Response({'errors': ['no college found with this id']}, status=404)

        return Response({'errors': ['you should be a superuser']}, status=403)


class AllCollegesView(APIView):

    def get(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            if request.user.is_superuser:
                colleges = College.objects.all()
            else:
                colleges = request.user.userprofile.colleges.all()

            serialized_colleges = CollegeSerializer(instance=colleges, many=True)
            return Response(serialized_colleges.data)

        return Response({'errors': ['you should login']}, status=403)


    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            serialized_college = CollegeSerializer(data=request.data)
            if serialized_college.is_valid():
                serialized_college.save()
                return Response(serialized_college.data, status=201)
            return Response(serialized_college.errors, status=400)

        return Response({'errors': ['you should be a superuser']}, status=403)


class CollegeRegister(APIView):

    def post(self, request, *args, **kwargs):
        college_id = request.data.get('college_id')
        if college_id:
            try:
                college = College.objects.get(id=college_id)
                if request.user.userprofile.colleges.filter(id=college_id).exists():
                    return Response({'errors': ['you have already registered in this college']}, status=400)
                if request.user.userprofile.balance >= college.price:
                    request.user.userprofile.balance -= college.price
                    request.user.userprofile.colleges.add(college)
                    request.user.userprofile.save()
                    return Response({'messages': ['registered successfully']}, status=200)
                else:
                    return Response({'errors': ['you have insufficient balance']}, status=400)
            except College.DoesNotExist:
                return Response({'errors': ['no college found with this id']}, status=404)

        return Response({'errors': ['you should specify college_id']}, status=400)
