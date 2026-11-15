from django.shortcuts import render
from django.views.generic import View
from json import loads
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class AdditionView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1+n2
        response_data={"addition_result":result}
        return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch")
class SubstractionView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1-n2 
        response_data={"substraction":result}
        return JsonResponse(response_data) 
@method_decorator(csrf_exempt,name="dispatch")
class SquareView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        a=form_data.get("side")
        area=a**2
        response_data={"area_of_square":area}
        return JsonResponse(response_data) 
@method_decorator(csrf_exempt,name="dispatch")
class RectangleView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        l=form_data.get("length")
        w=form_data.get("width")
        area=l*w
        response_data={"area_of_rectangle":area}
        return JsonResponse(response_data)                     

@method_decorator(csrf_exempt,name="dispatch")
class TriangleView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        b=form_data.get("base")
        h=form_data.get("height")
        area=1/2*b*h
        response_data={"area_of_triangle":area}
        return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch")
class CircleView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        r=form_data.get("radius")
        area=3.14159*r*r 
        response_data={"area_of_circle":area}
        return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch")
class ParallelogramView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        b=form_data.get("base")
        h=form_data.get("height")
        area=b*h
        response_data={"area_of_parallelogram":area}
        return JsonResponse(response_data)        


@method_decorator(csrf_exempt,name="dispatch")
class TrapeziumView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        a=form_data.get("side1")
        b=form_data.get("side2")
        h=form_data.get("height")
        area=1/2* (a+b) *h
        response_data={"area_of_trapezium":area}
        return JsonResponse(response_data)        

@method_decorator(csrf_exempt,name="dispatch")
class RhombusView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        b=form_data.get("base")
        h=form_data.get("height")
        area=b*h
        response_data={"area_of_rhombus":area}
        return JsonResponse(response_data)       

@method_decorator(csrf_exempt,name="dispatch")
class EllipseView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        a=form_data.get("semi-major")
        b=form_data.get("semi-minor")
        area=3.14159*a*b
        response_data={"area_of_ellipse":area}
        return JsonResponse(response_data)               