from rest_framework import serializers
from review_app.models import Review

class ReviewsSerializer(serializers.ModelSerializer):
    reviewer = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Review
        fields='__all__'
        #fields=['id','description','file','location','tel','type','user','working_hours','business_user','reviewer_id']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['reviewer'] = user
        review = Review.objects.create(**validated_data)

        return review