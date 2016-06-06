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

        tipsAndTricksManager.getAll().then(
            function(data) {
                vm.tips = data;
            },
            function(data) {
                alert(data);
            }
        );

        vm.toHumanDate=function(date){
        	var d=new Date(date);

			var finalDate=("0" + d.getDate()).slice(-2) + "-" + ("0"+(d.getMonth()+1)).slice(-2) + "-" +
    d.getFullYear() + " " + ("0" + d.getHours()).slice(-2) + ":" + ("0" + d.getMinutes()).slice(-2);

        	return finalDate;
        }

        vm.addTip = function() {
            tipsAndTricksManager.add(vm.tipToAdd).then(function() {
            	//Add to tips array
            	vm.tipToAdd.date_created=new Date();
                vm.tips.push(vm.tipToAdd);

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