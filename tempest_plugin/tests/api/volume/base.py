
import tempest.api.volume.base as base_tempest_volume
from lib.services.volume.v3 import availability_zone_client
from lib.services.volume.v3 import volumes_client
from lib.services.volume.v3 import backups_client
from lib.services.volume.v3 import services_client
from lib.services.volume.v3 import extensions_client
from lib.services.volume.v3 import limits_client
from lib.services.volume.v3 import snapshots_client
from lib.services.volume.v3 import scheduler_stats_client
from lib.services.volume.v3 import qos_client
from lib.services.volume.v3 import types_client
from lib.services.volume.v3 import hosts_client
from lib.services.volume.v3 import encryption_types_client
from lib.services.volume.v3 import quotas_client
from lib.services.volume.v3 import capabilities_client


class BaseVolumeTest(base_tempest_volume.BaseVolumeTest):
    @classmethod
    def skip_checks(cls):
        super(BaseVolumeTest, cls).skip_checks()

    @classmethod
    def setup_credentials(cls):
        super(BaseVolumeTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(BaseVolumeTest, cls).setup_clients()
        cls.client_manager = cls.get_client_manager(credential_type="primary")
        params = {"auth_provider": cls.client_manager.auth_provider,
                  "service": "volume",
                  "region": "RegionOne"}

        cls.availability_zone_client_v3 = \
            availability_zone_client.AvailabilityZoneClient(**params)
        cls.volumes_client_v3 = volumes_client.VolumesClient(**params)
        cls.backups_client_v3 = backups_client.BackupsClient(**params)
        cls.services_client_v3 = services_client.ServicesClient(**params)
        cls.volumes_extension_client_v3 = extensions_client.ExtensionsClient(
            **params)
        cls.volume_limits_client_v3 = limits_client.LimitsClient(**params)
        cls.snapshots_client_v3 = snapshots_client.SnapshotsClient(**params)
        cls.scheduler_stats_client_v3 =\
            scheduler_stats_client.SchedulerStatsClient(**params)
        cls.volume_qos_client_v3 = qos_client.QosSpecsClient(**params)
        cls.volume_types_client_v3 = types_client.TypesClient(**params)
        cls.hosts_client_v3 = hosts_client.HostsClient(**params)
        cls.encryption_types_client_3 = \
            encryption_types_client.EncryptionTypesClient(**params)
        cls.quotas_client_v3 = quotas_client.QuotasClient(**params)
        cls.capabilities_client_v3 = \
            capabilities_client.CapabilitiesClient(**params)

    @classmethod
    def resource_setup(cls):
        super(BaseVolumeTest, cls).resource_setup()

    @classmethod
    def resource_cleanup(cls):
        super(BaseVolumeTest, cls).resource_cleanup()


class BaseVolumeAdminTest(base_tempest_volume.BaseVolumeAdminTest):
    @classmethod
    def skip_checks(cls):
        super(BaseVolumeAdminTest, cls).skip_checks()

    @classmethod
    def setup_credentials(cls):
        super(BaseVolumeAdminTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(BaseVolumeAdminTest, cls).setup_clients()
        cls._setup_clients(credential_type="admin")
        cls._setup_clients(credential_type="primary")

    @classmethod
    def resource_setup(cls):
        super(BaseVolumeAdminTest, cls).resource_setup()

    @classmethod
    def resource_cleanup(cls):
        super(BaseVolumeAdminTest, cls).resource_cleanup()

    @classmethod
    def _setup_clients(cls, credential_type):
        if credential_type == "admin":
            cls.client_manager.os_adm = cls.get_client_manager(
                credential_type="admin")
            params = {"auth_provider": cls.client_manager.os_adm.auth_provider,
                      "service": "volume",
                      "region": "RegionOne"}

            cls.admin_availability_zone_client_v3 = \
                availability_zone_client.AvailabilityZoneClient(**params)
            cls.admin_volumes_client_v3 = \
                volumes_client.VolumesClient(**params)
            cls.admin_backups_client_v3 = \
                backups_client.BackupsClient(**params)
            cls.admin_services_client_v3 = \
                services_client.ServicesClient(**params)
            cls.admin_volumes_extension_client_v3 = \
                extensions_client.ExtensionsClient(**params)
            cls.admin_volume_limits_client_v3 = \
                limits_client.LimitsClient(**params)
            cls.admin_snapshots_client_v3 = \
                snapshots_client.SnapshotsClient(**params)
            cls.admin_scheduler_stats_client_v3 = \
                scheduler_stats_client.SchedulerStatsClient(**params)
            cls.admin_volume_qos_client_v3 = \
                qos_client.QosSpecsClient(**params)
            cls.admin_volume_types_client_v3 = \
                types_client.TypesClient(**params)
            cls.admin_hosts_client_v3 = hosts_client.HostsClient(**params)
            cls.admin_encryption_types_client_3 = \
                encryption_types_client.EncryptionTypesClient(**params)
            cls.admin_quotas_client_v3 = quotas_client.QuotasClient(**params)
            cls.admin_capabilities_client_v3 = \
                capabilities_client.CapabilitiesClient(**params)
        elif credential_type == "primary":
            cls.client_manager.os = cls.get_client_manager(
                credential_type="primary")
            params = {"auth_provider": cls.client_manager.os.auth_provider,
                      "service": "volume",
                      "region": "RegionOne"}

            cls.availability_zone_client_v3 = \
                availability_zone_client.AvailabilityZoneClient(**params)
            cls.volumes_client_v3 = volumes_client.VolumesClient(**params)
            cls.backups_client_v3 = backups_client.BackupsClient(**params)
            cls.services_client_v3 = services_client.ServicesClient(**params)
            cls.volumes_extension_client_v3 = \
                extensions_client.ExtensionsClient(**params)
            cls.volume_limits_client_v3 = \
                limits_client.LimitsClient(**params)
            cls.snapshots_client_v3 = \
                snapshots_client.SnapshotsClient(**params)
            cls.scheduler_stats_client_v3 = \
                scheduler_stats_client.SchedulerStatsClient(**params)
            cls.volume_qos_client_v3 = qos_client.QosSpecsClient(**params)
            cls.volume_types_client_v3 = types_client.TypesClient(**params)
            cls.hosts_client_v3 = hosts_client.HostsClient(**params)
            cls.encryption_types_client_3 = \
                encryption_types_client.EncryptionTypesClient(**params)
            cls.quotas_client_v3 = quotas_client.QuotasClient(**params)
            cls.capabilities_client_v3 = \
                capabilities_client.CapabilitiesClient(**params)
