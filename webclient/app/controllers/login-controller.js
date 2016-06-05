(function() {
    var loginController = function($rootScope, $location, userManager) {
        var vm = this;

        vm.signIn = function() {
            userManager.login(vm.user).then(function() {
                $rootScope.$broadcast('loggedIn', vm.user);
                vm.errorMessage = undefined;
                $location.path("/home");
            }, function(data) {
                vm.errorMessage = data;
            });
        }
    }

    angular.module("mainApp")
        .controller("loginController", ['$rootScope', '$location', "userManager", loginController]);

})();