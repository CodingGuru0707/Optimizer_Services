from django.db import models



# Create your models here.


class ChemicalElement(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'chemical_element'

    def __str__(self):
        return self.name

class ChemicalComps(models.Model):
    chem_ele = models.ForeignKey(ChemicalElement, on_delete=models.CASCADE, related_name='chemical_composition')
    percentage = models.FloatField()

    class Meta:
        db_table = 'compostions'

    def __str__(self):
        return f'{self.percentage} %' + ' of ' + f'{self.chem_ele}'



class Commodity(models.Model):
    name = models.CharField(max_length=100)
    inventory = models.FloatField()
    price = models.FloatField()
    chemical_composition = models.ManyToManyField(ChemicalComps, related_name='commodities')
    
    class Meta:
        db_table = 'commodity'


    def __str__(self):
        return '%d ---- %s' % (self.name, self.chemical_composition)


def get_valid_composition(self):
        for ele in self.chemical_composition.all():
            total = 0 
            total+=ele.percentage
        
        if total < 100:
            unknown = 100 - total
            unknown_ele = ChemicalComps.objects.create(chem_ele='unknown', percentage=unknown)
            final_comp = self.chemical_composition.add(unknown_ele)
            return super(Commodity, final_comp).save()
            
        elif total > 100:
            raise ValueError("Percentage out of range")
        else:
            return super(Commodity, total.chemical_composition).save()







            



    