ARG NETBOX_VARIANT=v3.6.8

FROM netboxcommunity/netbox:${NETBOX_VARIANT}

RUN mkdir -pv /plugins/netbox-physical-storage
COPY . /plugins/netbox-physical-storage

RUN /opt/netbox/venv/bin/python3 /plugins/netbox-physical-storage/setup.py develop && \
    cp -rf /plugins/netbox-physical-storage/netbox_physical_storage/ /opt/netbox/venv/lib/python3.11/site-packages/netbox_physical_storage
