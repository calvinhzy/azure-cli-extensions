#!/usr/bin/env bash
while IFS="," read -r ResourceGroupName ElasticSanName VolumeGroupName Name SizeGiB
do
  az elastic-san volume create --resource-group $ResourceGroupName --elastic-san $ElasticSanName --volume-group $VolumeGroupName --name $Name --size-gib $SizeGiB
done < <(tail -n +2 test.csv)