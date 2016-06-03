(function() {
    var loginController = function($location, userManager) {
        var vm = this;

        vm.signIn = function() {
            userManager.login(vm.user);
            $location.path("/home");
        }
    }

    angular.module("mainApp")
        .controller("loginController", ['$location', "userManager", loginController]);

})();