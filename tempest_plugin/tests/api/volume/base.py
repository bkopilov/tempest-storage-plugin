
import tempest.api.volume.base as base_tempest_volume
from lib.services.volume.v3 import availability_zone_client
from lib.services.volume.v3 import volumes_client


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
        auth_provider = cls.client_manager.auth_provider
        service_name="volume"
        region_name = "RegionOne"
        cls.availability_zone_client_v3 = \
            availability_zone_client.AvailabilityZoneClient(
                auth_provider,
                service=service_name,
                region=region_name)
        cls.volumes_client_v3 = volumes_client.VolumesClient(
            auth_provider,
            service=service_name,
            region=region_name)

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
        auth_provider = cls.client_manager.auth_provider
        service_name = "volume"
        region_name = "RegionOne"
        cls.admin_availability_zone_client_v3 = \
            availability_zone_client.AvailabilityZoneClient(
                auth_provider,
                service=service_name,
                region=region_name)

        cls.admin_volumes_client_v3 = volumes_client.VolumesClient(
            auth_provider,
            service=service_name,
            region=region_name)

    @classmethod
    def resource_setup(cls):
        super(BaseVolumeAdminTest, cls).resource_setup()

    @classmethod
    def resource_cleanup(cls):
        super(BaseVolumeAdminTest, cls).resource_cleanup()

