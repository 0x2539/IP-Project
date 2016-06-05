(function() {
    var registerController = function(userManager, $location) {
        var vm = this;

        vm.register = function() {
            userManager.register(vm.user).then(function() {
                $location.path("/home")
            }, function(data) {
                vm.errorMessage = data;
            });
        }

    }

    angular.module("mainApp")
        .controller("registerController", ['userManager', '$location', registerController]);

})();