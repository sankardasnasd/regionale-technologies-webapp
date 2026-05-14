from django.shortcuts import render, redirect

# Create your views here.


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate


# ====================== RENDER LOGIN PAGE (GET) ======================
def admin_login_page(request):
    return render(request, 'lognpage.html')




# ====================== ADMIN LOGIN API (POST) ======================
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate


@api_view(['POST'])
@permission_classes([AllowAny])
def admin_login_api(request):

    username = request.data.get("username")

    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    print(user)

    if user is not None:

        if user.groups.filter(name='admin').exists():

            return Response({

                "success": True,

                "message": "Admin Login Success",

                "user_id": user.id,

                "username": user.username,

                "email": user.email,

                "group": "admin"

            })

        else:

            return Response({

                "success": False,

                "message": "You are not an admin"

            })

    else:

        return Response({

            "success": False,

            "message": "Invalid Username or Password"

        })


from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response


def admin_logout_api(request):

    logout(request)

    return redirect('/myapp/admin_login_page/')

def home(request):
    return render(request,'admin/home.html')




from rest_framework.decorators import api_view

from rest_framework.response import Response

from .serializers import ContactSerializer
from rest_framework import status



@api_view(['GET'])
def contact_list(request):
    contacts = Contact.objects.all().order_by('-created_at')  # Latest first
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])

def contact_api(request):

    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response({

            "message":"Message Sent Successfully"

        })

    return Response(serializer.errors)


def contact_api_get(request):
    return render(request,'regional 2.html')


from django.shortcuts import render
from .models import Contact


def admindashboard(request):

    contacts = Contact.objects.all().order_by('-id')

    return render(request, 'admin_dashboard.html', {
        'contacts': contacts
    })





# views.py

from django.shortcuts import render

from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import Career

from .serializers import CareerSerializer


# ===================================
# HTML PAGE
# ===================================

def career_page(request):

    return render(
        request,
        'admin/careers.html'
    )


# ===================================
# ADD CAREER
# ===================================



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import CareerSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def add_career(request):

    print("DATA:", request.data)

    serializer = CareerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Career Added Successfully"})

    print(serializer.errors)
    return Response(serializer.errors, status=400)

# ===================================
# VIEW CAREERS
# ===================================

@api_view(['GET'])

def get_careers(request):

    careers = Career.objects.all()\
    .order_by('-id')

    print(careers)
    print('careers=========')
    print('careers=========')
    print('careers=========')
    print('careers=========')

    serializer = CareerSerializer(
        careers,
        many=True
    )

    return Response(serializer.data)


# ===================================
# DELETE CAREER
# ===================================

# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import Career


from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import Career



@csrf_exempt
@api_view(['DELETE'])
def delete_career(request, id):
    print(id,'career id-==-=--====')
    print(id,'career id-==-=--====')
    print(id,'career id-==-=--====')
    career = Career.objects.get(id=id)
    print(career)
    career.delete()
    return Response({
        "status": True,
        "message": "Career Deleted Successfully"
    })





@api_view(['GET'])
def public_get_careers(request):

    careers = Career.objects.all()\
    .order_by('-id')

    serializer = CareerSerializer(
        careers,
        many=True
    )

    return Response(serializer.data)


