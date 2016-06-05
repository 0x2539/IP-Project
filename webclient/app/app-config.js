(function() {

    var app = angular.module("mainApp");
    app.config(['$routeProvider', '$httpProvider',
        function($routeProvider, $httpProvider) {
            $routeProvider
                .when('/login', {
                    templateUrl: 'app/views/login.html',
                    controller: 'loginController as vm'
                })
                .when('/register', {
                    templateUrl: 'app/views/register.html',
                    controller: 'registerController as vm'
                })
                .when('/home', {
                    templateUrl: 'app/views/home.html',
                    controller: 'homeController as vm'
                })
                .otherwise({
                    redirectTo: '/home'
                });

            $httpProvider.interceptors.push('authenticationInterceptor');
        }
    ]);
})();