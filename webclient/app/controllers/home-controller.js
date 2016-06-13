(function() {
    var homeController = function($timeout, categoriesManager, tipsAndTricksManager, ratingManager) {
        var vm = this;
        vm.starRating1 = 4;
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

        vm.toHumanDate = function(date) {
            var d = new Date(date);

            var finalDate = ("0" + d.getDate()).slice(-2) + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" +
                d.getFullYear() + " " + ("0" + d.getHours()).slice(-2) + ":" + ("0" + d.getMinutes()).slice(-2);

            return finalDate;
        }

        vm.addTip = function() {
            tipsAndTricksManager.add(vm.tipToAdd).then(function() {
                //Add to tips array
                vm.tipToAdd.date_created = new Date();
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

        vm.rate = function(tip) {
            ratingManager.apply(tip.id, tip.rating);
                tip.number_of_ratings++;
                tip.average_rating = tip.average_rating + ((tip.rating - tip.average_rating) / tip.number_of_ratings);

        }
        vm.formatNumber = function(i) {
            return Math.round(i * 100) / 100;
        }
    }

    angular.module("mainApp")
        .controller("homeController", ['$timeout', 'categoriesManager', 'tipsAndTricksManager', 'ratingManager', homeController]);

})();