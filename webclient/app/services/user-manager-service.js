(function() {

    function userManager($cookies, $http, constants) {
        var login = function(user) {
            $http({
                method: 'POST',
                url: constants.baseUrl + "login",
                data: user,
                unauthenticated: true
            }).then(function success(response) {
                alert(response.data.token);
                $cookies.put(constants.cookie_key, response.data.token);
            }, function error(response) {
                alert(response.data.error);
            });
        }

        var register = function(user) {
            $http({
                method: 'PUT',
                url: constants.baseUrl + "create-account",
                data: user,
                unauthenticated: true
            }).then(function success(response) {
                alert(JSON.stringify(response.data));
            }, function error(response) {
                alert(response.data.error)
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