(function() {

    var app = angular.module("mainApp", ["ngRoute", "ngCookies"]);

    app.constant('constants', {
        baseUrl: 'http://127.0.0.1:8000/',
        cookie_key: "token_cookie"
    });
})();