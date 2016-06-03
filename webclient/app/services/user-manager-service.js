(function() {

    function userManager($cookies, $http, constants) {
        var login = function(user) {
            $http({
                method: 'POST',
                url: constants.baseUrl + "login",
                data: user,
                unauthenticated: true
            }).then(function success(response) {
                $cookies.put(constants.cookie_key, response.data)
            }, function error(response) {
                alert(response.data)
            });
        }

        var register = function(user) {
            $http({
                method: 'PUT',
                url: constants.baseUrl + "create-account",
                data: user,
                unauthenticated: true
            }).then(function success(response) {
                alert(response.data);
            }, function error(response) {
                alert(response.data)
            });
        }

        return {
            login: login,
            register: register
        }
    }

    angular.module("mainApp")
        .factory("userManager", ['$cookies', '$http', 'constants', userManager]);

})();