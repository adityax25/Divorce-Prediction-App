from django.db import models
import json
# Create a model to store the form data to re-train a better model.

class Data(models.Model):
    data_dict = models.CharField(max_length=511,default=json.dumps({}))
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    prediction = models.BooleanField()
    true_result = models.BooleanField(blank=True,null=True)
    def set_data(self, dict):
        self.data_dict = json.dumps(dict)
    def get_data(self):
        return json.loads(self.data_dict)
    