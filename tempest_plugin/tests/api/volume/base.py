
import tempest.api.volume.base as base_tempest_volume
from lib.services.volume.v3 import availability_zone_client
from lib.services.volume.v3 import volumes_client
from lib.services.volume.v3 import backups_client
from lib.services.volume.v3 import services_client
from lib.services.volume.v3 import extensions_client
from lib.services.volume.v3 import limits_client
from lib.services.volume.v3 import snapshots_client


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
        cls.client_manager = cls.get_client_manager()
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
        cls.client_manager = cls.get_client_manager()
        params = {"auth_provider": cls.client_manager.auth_provider,
                  "service": "volume",
                  "region": "RegionOne"}

        cls.admin_availability_zone_client_v3 = \
            availability_zone_client.AvailabilityZoneClient(**params)
        cls.admin_volumes_client_v3 = volumes_client.VolumesClient(**params)
        cls.admin_backups_client_v3 = backups_client.BackupsClient(**params)
        cls.admin_services_client_v3 = services_client.ServicesClient(**params)
        cls.admin_volumes_extension_client_v3 =\
            extensions_client.ExtensionsClient(**params)
        cls.admin_volume_limits_client_v3 = \
            limits_client.LimitsClient(**params)
        cls.admin_snapshots_client_v3 = \
            snapshots_client.SnapshotsClient(**params)

    @classmethod
    def resource_setup(cls):
        super(BaseVolumeAdminTest, cls).resource_setup()

    @classmethod
    def resource_cleanup(cls):
        super(BaseVolumeAdminTest, cls).resource_cleanup()
