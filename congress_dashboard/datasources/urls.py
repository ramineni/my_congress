# Copyright 2014 VMware.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.conf.urls import patterns
from django.conf.urls import url

from congress_dashboard.datasources import views


SERVICES = (
    r'^services/(?P<datasource_id>[^/]+)/(?P<service_table_name>[^/]+)/%s$')
POLICIES = (
    r'^policies/(?P<datasource_id>[^/]+)/(?P<policy_table_name>[^/]+)/%s$')

DATASOURCE = r'^(?P<datasource_id>[^/]+)/detail/$'

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(SERVICES % 'detail', views.DetailView.as_view(),
        name='datasource_table_detail'),
    url(DATASOURCE, views.DatasourceView.as_view(),
        name='datasource_detail'),
    url(POLICIES % 'detail', views.DetailView.as_view(),
        name='policy_table_detail'),
)
