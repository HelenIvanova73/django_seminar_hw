from django.shortcuts import render, HttpResponse
from django.views import View


# Create your views here.

class IndexView(View):
    def get(self, request):
        return HttpResponse(
            '''
 <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Company Name</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="#">Company Name</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">About Us</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Products</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="container mt-4">
        <h1>Welcome to Company Name</h1>
        <p>Discover our innovative products and services that cater to your needs. We strive for excellence and
            customer satisfaction.</p>

        <h2>About Us</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod, libero a tincidunt rhoncus, ipsum
            tortor
            accumsan felis, at aliquet elit quam et libero. Curabitur auctor vitae est sit amet tincidunt. Sed in mi
            eu
            metus convallis facilisis. Duis at libero vel elit varius volutpat. Ut vel interdum odio.</p>
    </div>

    <!-- Footer -->
    <footer class="bg-dark text-light text-center py-3">
        <p>&copy; 2024 Company Name. All rights reserved.</p>
    </footer>

    <!-- Bootstrap JS (optional, if you need features like the navbar toggler) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>
            '''
        )


class Contact(View):
    def get(self, request):
        context =  '''
                    <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Contact Us</title>
            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>

        <body>
            <!-- Navbar -->
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <div class="container">
                    <a class="navbar-brand" href="#">Company Name</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav ml-auto">
                            <li class="nav-item">
                                <a class="nav-link" href="#">Home</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">Products</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">Contact</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>

            <!-- Main Content -->
            <div class="container mt-4">
                <h1>Contact Us</h1>
                <p>If you have any questions, feel free to reach out to us.</p>
                <!-- Contact Information -->
                <div class="row">
                    <div class="col-md-6">
                        <h3>Contact Details</h3>
                        <p>Email: info@company.com</p>
                        <p>Phone: +1 (555) 123-4567</p>
                    </div>
                    <div class="col-md-6">
                        <!-- Map or additional contact details can go here -->
                    </div>
                </div>
            </div>

            <!-- Footer -->
            <footer class="bg-dark text-light text-center py-3">
                <p>&copy; 2024 Company Name. All rights reserved.</p>
            </footer>

            <!-- Bootstrap JS (optional, if you need features like the navbar toggler) -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        </body>

        </html>

                    '''
        return HttpResponse(
            context
        )