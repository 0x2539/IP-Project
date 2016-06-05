(function() {

    function globalController($scope, userManager, $location) {
        var vm = this;

        vm.loggedIn = false;
        vm.userName = undefined;

        $scope.$on('loggedIn', function(event, args) {
            vm.loggedIn = true;
            vm.userName = args.email;
        });

        vm.logout = function() {
            userManager.logout();
            vm.loggedIn = false;
            $location.path('/login');
        }
    }

    angular.module("mainApp")
        .controller("globalController", ['$scope', 'userManager', '$location', globalController]);
})();