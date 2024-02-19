from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from library.models import Library
from .serializers import BookSerializer,CheckoutSerializer
from django.utils import timezone
from rest_framework.decorators import api_view
from django.http import JsonResponse


class BookListApiView(APIView):
    def get(self,request):
        books = Library.objects.all()
        if len(books) == 0:
            return Response({'message':'Books Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        limit = self.request.query_params.get('limit')
        if limit:
            try:
                limit = int(limit)
                books = books[:limit]
            except ValueError:
                pass

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ChekoutApiView(APIView):
    def post(self,request):
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            book_id = serializer.validated_data.get('book_id')
             
            try:
                book = Library.objects.get(pk=book_id)
                if book.is_in_stock:
                    book.date_checked_out = timezone.now()
                    book.is_in_stock = False
                    book.save()
                    
                    updated_row_html = f'<tr id=row-{book_id}><td>{book.titlle}</td><td>{book.author}</td><td>{book.publisher}</td><td>{book.category}</td><td>{book.page_count}</td><td>{book.shelf_location}</td><td>{book.publish_date}</td><td>No</td><td><span>Already Checkout</span></td></tr>'

                    return JsonResponse({'row_html': updated_row_html, 'book_id': book_id})
                else:
                    return Response({'message': 'Book is not available for checkout'}, status=status.HTTP_400_BAD_REQUEST)
            except Library.DoesNotExist:
                return Response({'message':'Book Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def checkout(request, *args, **kwargs):
        if request.method != 'POST':
            return JsonResponse({'success': False, 'message': 'Invalid request method'}, status.HTTP_405_METHOD_NOT_ALLOWED)
        
        serializer = CheckoutSerializer(data=request.POST)
        if serializer.is_valid():
            book_id = serializer.validated_data.get('book_id')
            try:
                book = Library.objects.get(pk=book_id)
                if book.is_in_stock:
                    book.date_checked_out = timezone.now()
                    book.is_in_stock = False
                    book.save()
                    updated_row_html = f'<tr id=row-{book.id}><td>{book.titlle}</td><td>{book.author}</td><td>{book.publisher}</td><td>{book.category}</td><td>{book.page_count}</td><td>{book.shelf_location}</td><td>{book.publish_date}</td><td>No</td><td><span>Already Checkout</span></td></tr>'
                    return JsonResponse({'row_html': updated_row_html, 'book_id': book_id})
                else:
                    return Response({'message': 'Book is not available for checkout'}, status=status.HTTP_400_BAD_REQUEST)
            except Library.DoesNotExist:
                return Response({'message':'Book Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)