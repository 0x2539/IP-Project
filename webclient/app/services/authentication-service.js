(function() {
    var authenticationInterceptor = function($cookies, $location, constants) {
        var onRequest = function(config) {
            if (typeof config.unauthenticated === 'undefined' || config.unauthenticated)
                return config;


            if (typeof $cookies.getObject(constants.cookie_key) !== 'undefined') {
                config.headers.Authorization = 'Bearer ' + $cookies.getObject(cookie_key);
            } else {
                $location.path('/login');
            }
            return config;
        }

        var onResponse = function(response) {
            if (response.status === '403') {
                $location.path('/login');
            }
            return response;
        }

        return {
            request: onRequest,
            response: onResponse
        };
    }

    angular.module("mainApp")
        .factory("authenticationInterceptor", ['$cookies', '$location', 'constants', authenticationInterceptor]);

})();