from django.db import models

# Create your models here.


class Timeline(models.Model):
    webcast_liftoff = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    go_for_prop_loading = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    stage1_rp1_loading = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    stage2_rp1_loading = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    rp1_loading = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    stage1_lox_loading = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    stage2_lox_loading = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    engine_chill = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    prelaunch_checks = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    propellant_pressurization = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    go_for_launch = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    ignition = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    liftoff = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    maxq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    beco = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    meco = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    side_core_sep = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    side_core_boostback = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    center_stage_sep = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    fairing_deploy = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    stage_sep = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    second_stage_ignition = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    side_core_entry_burn = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    seco1 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    seco2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    seco3 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    seco4 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    side_core_landing = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    center_core_entry_burn = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    center_core_landing = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    payload_deploy = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    second_stage_restart = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    dragon_separation = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    dragon_solar_deploy = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    dragon_bay_door_deploy = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    first_stage_boostback_burn = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    first_stage_entry_burn = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    first_stage_landing_burn = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    first_stage_landing = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    webcast_launch = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    payload_deploy_1 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    payload_deploy_2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    center_core_boostback = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    def __str__(self):
        return str(self.webcast_liftoff)