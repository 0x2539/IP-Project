(function() {

    function userManager($cookies, $http, $q, constants) {
        var login = function(user) {
            var deferred = $q.defer();
            $http({
                method: 'POST',
                url: constants.baseUrl + "login",
                data: user,
                unauthenticated: true
            }).then(function success(response) {
                $cookies.put(constants.cookie_key, response.data.token);
                deferred.resolve();
            }, function error(response) {
                deferred.reject("Login failed");
            });
            return deferred.promise;
        }

        var register = function(user) {
            var deferred = $q.defer();
            $http({
                method: 'PUT',
                url: constants.baseUrl + "create-account",
                data: user,
                unauthenticated: true
            }).then(function success(response) {
                deferred.resolve();
            }, function error(response) {
                deferred.reject("Register failed");
            });
            return deferred.promise;
        }

        var logout = function() {
            $cookies.remove(constants.cookie_key)
        }

        return {
            login: login,
            register: register,
            logout: logout
        }
    }

    angular.module("mainApp")
        .factory("userManager", ['$cookies', '$http', '$q', 'constants', userManager]);

})();