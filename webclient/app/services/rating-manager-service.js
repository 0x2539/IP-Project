(function() {

    function ratingManager($http, $q, constants) {
        var apply = function(id, rating) {
            var deferred = $q.defer();
            $http({
                method: 'PUT',
                url: constants.baseUrl + "rating_apply",
                data: {
                    tip_and_trick_id: id,
                    rating: rating,
                    comment: ""
                },
                unauthenticated: false,
            }).then(function success(response) {
                deferred.resolve();
            }, function error(response) {
                deferred.reject("Tip add failed");
            });
            return deferred.promise;
        }

        return {
            apply: apply
        };
    }

    angular.module("mainApp")
        .factory("ratingManager", ['$http', '$q', 'constants', ratingManager]);

})();