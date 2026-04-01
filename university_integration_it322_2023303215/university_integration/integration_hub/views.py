import urllib.request
import json
from rest_framework.views import APIView
from rest_framework.response import Response

class StudentIntegrationSummary(APIView):
    def get(self, request, student_id):
        base_url = "http://127.0.0.1:8000/api"
        
        try:
            # 1. Fetch from Student App
            with urllib.request.urlopen(f"{base_url}/students/") as response:
                students = json.loads(response.read().decode())
            student_data = next((s for s in students if s['student_id'] == student_id), None)
            
            if not student_data:
                return Response({"error": "Student not found in Student App"}, status=404)
                
            # 2. Fetch from Library App
            with urllib.request.urlopen(f"{base_url}/library/") as response:
                library_records = json.loads(response.read().decode())
            student_library = next((l for l in library_records if l['student_id'] == student_id), None)
            
            # 3. Fetch from Payment App
            with urllib.request.urlopen(f"{base_url}/payments/") as response:
                payments = json.loads(response.read().decode())
            student_payments = [p for p in payments if p['student_id'] == student_id]
            
            # Data Transformation & Consolidation Pattern
            consolidated_data = {
                "student_profile": {
                    "id": student_data['student_id'],
                    "full_name": student_data['name'],
                    "enrolled_course": student_data['course'],
                    "contact_email": student_data['email']
                },
                "library_status": {
                    "has_fines": student_library['has_fines'] if student_library else False,
                    "fine_amount": student_library['amount_due'] if student_library else "0.00"
                },
                "billing_history": [
                    {"amount": p['amount_paid'], "date": p['date_paid']} for p in student_payments
                ]
            }
            
            return Response(consolidated_data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
