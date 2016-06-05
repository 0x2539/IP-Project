(function() {
    var homeController = function($timeout, categoriesManager, tipsAndTricksManager) {
        var vm = this;
        categoriesManager.getAll().then(
            function(data) {
                vm.categories = data;
            },
            function(data) {
                alert(data);
            }
        );

        vm.addTip = function() {
            tipsAndTricksManager.add(vm.tipToAdd).then(function() {
                vm.showAlert = true;
                vm.alertMessage = "Tip added successfully";
                closeOnTimeout(3000);
                vm.tipToAdd = undefined;
            })
        }

        closeOnTimeout = function(timeout) {
            $timeout(function() {
                vm.showAlert = false;
                vm.alertMessage = "";
            }, timeout);
        }
    }

    angular.module("mainApp")
        .controller("homeController", ['$timeout', 'categoriesManager', 'tipsAndTricksManager', homeController]);

})();