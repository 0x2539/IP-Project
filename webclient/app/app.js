(function() {

    var app = angular.module("mainApp", ["ngRoute", "ngCookies", "angular-input-stars"]);

    app.constant('constants', {
        baseUrl: 'http://127.0.0.1:8000/',
        cookie_key: "token_cookie",
        user_email: "user_email_cookie"
    });

    app.run(function($cookies, $rootScope, $timeout, constants) {
        if ($cookies.get(constants.cookie_key) && $cookies.get(constants.user_email)) {
            $timeout(function() {
                $rootScope.$broadcast('loggedIn', {
                    email: $cookies.get(constants.user_email)
                });
            }, 100)
        }
    })
})();