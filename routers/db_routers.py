class AuthRouter:
    route_app_labels = ['auth','contenttypes','sessions','admin','Users']
    
    def _db_for_action(self, model, **hints):
        """Route to our database if one of our apps."""

        if model._meta.app_label in self.route_app_labels:
            return 'default_db'

        return None

    db_for_read = _db_for_action
    db_for_write = _db_for_action
   

    def allow_relation(self,obj1,obj2,**hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None
        
    
    def allow_migrate(self,db,app_label,model_name = None,**hints):
        if (app_label in self.route_app_labels):
            return db =='default_db'
        return None



class ProductRouter:
    route_app_labels = ['Products',]


    def _db_for_action(self, model, **hints):
        """Route to our database if one of our apps."""

        if model._meta.app_label in self.route_app_labels:
            return 'product_db'

        return None
    

    db_for_read = _db_for_action
    db_for_write = _db_for_action

    def allow_relation(self,obj1,obj2,**hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self,db,app_label,model_name = None,**hints):
        if (app_label in self.route_app_labels):
            return db =='product_db'
        return None