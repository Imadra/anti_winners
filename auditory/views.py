from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, api_view
from datetime import datetime


from .models import Auditory, Booking


def kuhn(n, k, g):
    print(" --  ")
    print(n)
    print(k)
    print(g)
    print(" ---")
    used = [0] * n
    mt = [-1] * k

    def try_kuhn(v):
        if used[v]:
            return False
        used[v] = True
        for i in range(len(g[v])):
            to = g[v][i]
            if mt[to] == -1 or try_kuhn(mt[to]):
                mt[to] = v
                return True
        return False

    for v in range(n):
        used = [0] * n
        try_kuhn(v)

    ans = []

    for i in range(k):
        if mt[i] != -1:
            # print("{} {}".format(mt[i], i))
            ans.append((mt[i], i))
    return ans


@permission_classes([])#IsAuthenticated])
class AddAuditory(APIView):
    def post(self, request):
        print(request.data)
        Auditory.objects.create(**request.data)
        return Response(status=status.HTTP_200_OK, data="Codeforces red auditory")

@permission_classes([])  # IsAuthenticated])
class AddBooking(APIView):
    def post(self, request):
        print(request.data)
        Booking.objects.create(**request.data)
        return Response(status=status.HTTP_200_OK, data="Codeforces red booking")


def logg(data, text):
    print()
    print("   -  " + text)
    print(data)
    print()


@permission_classes([])#IsAuthenticated])
class Distribute(APIView):
    def get(self, request):
        bookings = list(Booking.objects.filter(time_from__gt=datetime.now()).order_by('time_from'))
        available_auditories = list(Auditory.objects.all())
        reserved_auditories = list()
        bookings_i = 0

        while bookings_i < len(bookings):
            to_book = list()
            booking_time = bookings[bookings_i].time_from
            while bookings_i < len(bookings) and bookings[bookings_i].time_from == booking_time:
                to_book.append(bookings[bookings_i])
                bookings_i += 1

            new_reserved = []
            for to_time, auditory in reserved_auditories:
                if to_time > booking_time:
                    new_reserved.append((to_time, auditory))
                else:
                    available_auditories.append(auditory)
            reserved_auditories = new_reserved
            # logg(reserved_auditories, "reserved")
            # logg(available_auditories, "avail")

            edge_weights = [[to_book[i].calculate_edge_with(available_auditories[j]) for j in range(len(available_auditories))] for i in range(len(to_book))]
            logg(edge_weights, "edge weights")
            logg([[(to_book[i].id, available_auditories[j].id) for j in range(len(available_auditories))] for i in range(len(to_book))], "index")
            for weight in range(1, 11):
                g = []
                for i in range(len(to_book)):
                    g.append([])
                    for j in range(len(available_auditories)):
                        if round(edge_weights[i][j], 1) == round(weight / 10, 1):
                            g[i].append(j)
                filtered_edges = kuhn(len(to_book), len(available_auditories), g)
                logg(filtered_edges, "filtered edges")

                new_available_auditories = []
                for i, j in filtered_edges:
                    to_book[i].set_auditory(available_auditories[j])
                    reserved_auditories.append((to_book[i].time_till, available_auditories[j]))
                for t in range(len(available_auditories)):
                    p = 1
                    for i, j in filtered_edges:
                        if t == j:
                            p = 0
                            break
                    if p == 1:
                        new_available_auditories.append(available_auditories[t])
                available_auditories = new_available_auditories
        return Response(status=status.HTTP_200_OK, data="OK")






# @permission_classes([IsAuthenticated])
# class CheckToken(APIView):
#     def post(self, request):
#         return Response(status=status.HTTP_200_OK, data=request.user.username)

# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("email")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key}, status=status.HTTP_200_OK)

# @permission_classes([])
# class Register(APIView):
#     def post(self, request):
#         password = request.data.get("password")
#         first_name = request.data.get("first_name")
#         last_name = request.data.get("last_name")
#         email = request.data.get("email")
#         username = email
#         print(email)
#         if username is None or username == "":
#             return Response(status=status.HTTP_400_BAD_REQUEST, data="Email is not provided")
#         if password is None:
#             return Response(status=status.HTTP_400_BAD_REQUEST, data="password is not provided")
#         if first_name is None:
#             return Response(status=status.HTTP_400_BAD_REQUEST, data="first_name is not provided")
#         if last_name is None:
#             return Response(status=status.HTTP_400_BAD_REQUEST, data="last_name is not provided")
#         check = User.objects.filter(username=username)
#         if len(check) > 0:
#             return Response(status=status.HTTP_400_BAD_REQUEST, data="username exists")
#         user = User.objects.create_user(username, email, password)
#         user.first_name = first_name
#         user.last_name = last_name
#         user.save()
#         token = TokenSerializer(Token.objects.get(user=user))
#         return Response(status=status.HTTP_200_OK, data=token.data)

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)