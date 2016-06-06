(function() {

    function tipsAndTricksManager($http, $q, constants) {
        var add = function(tip) {
            var deferred = $q.defer();
            $http({
                method: 'PUT',
                url: constants.baseUrl + "tip_and_trick",
                data: tip,
                unauthenticated: false,
            }).then(function success(response) {
                deferred.resolve();
            }, function error(response) {
                deferred.reject("Tip add failed");
            });
            return deferred.promise;
        }

        var getAll = function() {
            var deferred = $q.defer();

            $http({
                method: 'GET',
                url: constants.baseUrl + "tip_and_trick",
                unauthenticated: false,
            }).then(function success(response) {
                deferred.resolve(response.data);
            }, function error(response) {
                deferred.reject("Tips get failed " + response.data);
            });
            return deferred.promise;
        }

        return {
            add: add,
            getAll:getAll
        };
    }

    angular.module("mainApp")
        .factory("tipsAndTricksManager", ['$http', '$q', 'constants', tipsAndTricksManager]);

})();