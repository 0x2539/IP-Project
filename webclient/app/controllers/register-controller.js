(function() {
    var registerController = function(userManager) {
        var vm = this;

        vm.register = function() {
            userManager.register(vm.user);
        }

    }

    angular.module("mainApp")
        .controller("registerController", ["userManager", registerController]);

})();